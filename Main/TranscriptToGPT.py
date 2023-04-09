import os
import openai
import math
import customtkinter as ct
from PrepareTranscript import get_transcript
from MP3ToTranscript import determine_video_type, large_video, small_video
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")


def populate_summaries(option, file_path, raw_transcript, youtube_url):
    if option in (0, 1, 2):
        BATCHES = get_transcript(option, file_path, raw_transcript, youtube_url)
        print("BEFORE: " + str(BATCHES))
        if BATCHES is not None and len(BATCHES) != 0:
            print("POPULATE SUMMARIES: " + str(len(BATCHES)))
            summaries = []
            for batch in BATCHES:
                with open(batch, "r") as f:
                    summaries.append(createPartitionedSummary(str(f.read())))
            return summaries
        
    

def practce_problems(summary, outputTextBox):
    gpt_prompt = "Give me a few practice problems and an answer key for the problems based on the following summary:\n\n" + summary
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    with open("Practice_Problems.txt", "w") as f:
        f.write(response.choices[0].text)
        outputTextBox.insert("1.0", str(response.choices[0].text))
  
    return response.choices[0].text

def notes(summary, outputTextBox):
    gpt_prompt = "Give me a whole page's worth of nicely formatted notes, using proper spacing, titles, and bullet points based on the following summary:\n\n" + summary
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    with open("Notes.txt", "w") as f:
        f.write(response.choices[0].text)
        outputTextBox.insert("1.0", str(response.choices[0].text))

    return response.choices[0].text

def summary(summaries, outputTextBox):
    transcript = ""
    for summary in summaries:
        transcript += summary
    with open("Summary.txt", "w") as f:
        f.write(transcript)
        outputTextBox.insert("1.0", str(transcript))

    return transcript


def createPartitionedSummary(partitionedTranscript):
    maxChar = math.floor(2000 / 6) # 2000 is the safe amount for max character length
    gpt_prompt = "Give me a summary that has a hard max of " + str(maxChar) + """ characters, but try to  
                 "make it as detailed as possible for this transcript (don't mention that this is a transcript summary):\n\n""" + partitionedTranscript
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    return response.choices[0].text


def stichSummaries(summaries):
    """
    This function, although a work of pure art is seriously inconsistent with the summaries
    """
    transcript = ""
    for summary in summaries:
        transcript += summary
    print(transcript)
    gpt_prompt = "Give me an 8-sentence long summary that is very detailed based on this transcript:\n\n""" + transcript
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    return response.choices[0].text






