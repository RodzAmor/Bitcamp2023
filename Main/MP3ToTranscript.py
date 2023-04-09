import os
import openai
from dotenv import load_dotenv
from pydub import AudioSegment
import json

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")


def large_video(file_name):
    PARTITION_SIZE = 22

    # 1,048,576 = 1mb
    MB_SIZE = 1000000

    audio_file = AudioSegment.from_mp3(file_name)

    file_size_MB = os.path.getsize(file_name)/MB_SIZE
    partitions = int(file_size_MB / PARTITION_SIZE) + 1
    seconds_per_chunk = int(audio_file.duration_seconds / (file_size_MB / PARTITION_SIZE)) 
    seconds_per_chunk *= 1000
    
    full_transcript = ""
    for i in range(0, partitions):
        audio_chunk = audio_file[i * seconds_per_chunk:(i+1)*seconds_per_chunk]
        audio_chunk.export(f'chunk_{i}.mp3', format='mp3')

        audio_chunk_file = open(f"chunk_{i}.mp3", "rb")
        transcript_chunk = str(openai.Audio.transcribe("whisper-1", audio_chunk_file))

        full_transcript += json.loads(transcript_chunk)["text"]

        audio_chunk_file.close()
        os.remove(f"chunk_{i}.mp3")
    return full_transcript.text


def small_video(file_name):
    audio_file = open(file_name, "rb")
    
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    audio_file.close()
    return transcript.text


def determine_video_type(file_name):
    # 1,048,576 = 1mb
    MB_SIZE = 1000000
    if (os.path.getsize(file_name) < (25 * MB_SIZE)):
        return small_video()
    else:
        return large_video()
