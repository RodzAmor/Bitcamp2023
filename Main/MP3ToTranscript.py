import os
import openai
from dotenv import load_dotenv
from pydub import AudioSegment
import json

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

PARTITION_SIZE = 22

# 1,048,576 = 1mb
MB_SIZE = 1000000
FILE_NAME = "sound.mp3"
def large_video():
    audio_file = AudioSegment.from_mp3(FILE_NAME)

    file_size_MB = os.path.getsize(FILE_NAME)/MB_SIZE
    partitions = int(file_size_MB / PARTITION_SIZE) + 1
    seconds_per_chunk = int(audio_file.duration_seconds / (file_size_MB / PARTITION_SIZE)) 
    # print("file size:", file_size_MB)
    # print("video duration: ", audio_file.duration_seconds)
    # print("# of chunks:", partitions)
    # print("seconds per chunk:", seconds_per_chunk)
    seconds_per_chunk *= 1000
    
    full_transcript = ""
    for i in range(0, partitions):
        audio_chunk = audio_file[i * seconds_per_chunk:(i+1)*seconds_per_chunk]
        audio_chunk.export(f'chunk_{i}.mp3', format='mp3')

        audio_chunk_file = open(f"chunk_{i}.mp3", "rb")
        transcript_chunk = str(openai.Audio.transcribe("whisper-1", audio_chunk_file))

        full_transcript += json.loads(transcript_chunk)["text"]

        audio_chunk_file.close()
    print(full_transcript)
    os.system("rm -f chunk*")


def small_video():
    audio_file = open(FILE_NAME, "rb")
    
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    audio_file.close()


if(os.path.getsize(FILE_NAME) < (25 * MB_SIZE)):
    small_video()
else:
    large_video()