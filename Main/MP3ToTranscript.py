import os
import openai
from dotenv import load_dotenv
# from pydub import AudioSegment

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

audio_file = open("test.mp3", "rb")
# mp3 = AudioSegment.from_mp3("test.mp3")

# print(mp3.duration_seconds)

# ten_minutes = 10 * 60 * 1000
# first_10_minutes = mp3[:ten_minutes]

transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)

