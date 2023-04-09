import re
from MP3ToTranscript import determine_video_type
from YoutubeDownload import convert_youtube_link

def get_transcript(option, file_path=None, raw_transcript=None, youtube_url=None):
    """
    option= 0: upload file
    option= 1: paste transcript
    option= 2: youtube URL
    anything else will simply not cause anything
    """
    if (option == 0):
        if (file_path is not None):
            raw = determine_video_type(file_path)
            direct_transcript(raw)
            return partition_transcript()
    elif (option == 1):
        if (raw_transcript is not None):
            direct_transcript(raw_transcript)
            return partition_transcript()
    elif (option == 2):
        if (youtube_url is not None):
            convert_youtube_link(youtube_url)
            raw = determine_video_type("Youtube.mp3")
            direct_transcript(raw)
            return partition_transcript()
    else:
        return None


def direct_transcript(raw):
    with open("Transcript.txt", "w") as f:
        f.write(raw)
    
    pattern = r'\b(?:\d{1,2}:)?(?:\d{1,2}:)?\d{1,2}\b'

    with open('Transcript.txt', 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if re.match(pattern, line.strip()):  # remove line if only timestamp
            continue
        else:
            new_lines.append(re.sub(pattern, '', line))  # remove timestamp only

    with open('Transcript.txt', 'w') as f:
        f.writelines(new_lines)

def partition_transcript():
    charCount = 0
    batchCount = 0
    batches = []
    with open('Transcript.txt', 'r') as f:
        lines = f.readlines()
        currentBatch = []
        for line in lines:
            charCount += len(line)
            currentBatch.append(line)
            if (charCount >= 4000):
                fname = 'batch' + str(batchCount) + '.txt'
                batches.append(fname)
                with open(fname, 'w') as batch:
                    batch.writelines(currentBatch)                    
                # reset the count and current batch list for the next batch
                currentBatch.clear()
                charCount = 0
                batchCount += 1
    return batches
    
