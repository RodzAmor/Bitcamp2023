import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")

# Keep in mind the audiofile should be less than 25 mb
# If you want an input longer than 25 mb, use the pydub library
audio_file = open("test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)

