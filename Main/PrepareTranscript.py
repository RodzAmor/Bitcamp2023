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
            raw = determine_video_type("Youtube_Video.mp3")
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
    batches = []
    list = []
    with open('Transcript.txt', 'r') as f:
        raw = str(f.read())
        batches = [raw[i:i+4000] for i in range(0, len(raw), 4000)]
        for i in range(len(batches)):
            with open('batch' + str(i) + '.txt', "w") as f:
                f.write(batches[i])
                list.append('batch' + str(i) + '.txt')
    return list

