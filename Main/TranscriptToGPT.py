import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

audio_file = open("test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

while (True):
    user_prompt = input("Would you like a summary, notes, or practice problems? ").lower()
    gpt_prompt = "Give me "

    if (user_prompt == "summary"):
        gpt_prompt += "a 3-sentence long summary based on the following transcript:\n\n"
    elif (user_prompt == "notes"):
        gpt_prompt += "a whole page's worth of nicely formatted notes, using proper spacing, titles, and bullet points based on the following transcript:\n\n" 
    elif (user_prompt == "practice problems"):
        gpt_prompt += "practice problems and an answer key for the problems based on the following transcript:\n\n"
    else:
        print("That is not an option!")
        exit(0)

    gpt_prompt += transcript.text        

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    print(response.choices[0].text)








