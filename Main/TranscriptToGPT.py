import os
import openai
import math
from PrepareTranscript import batches
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

#audio_file = open("test.mp3", "rb")
#transcript = openai.Audio.transcribe("whisper-1", audio_file)



def main():
    summaries = []
    for batch in batches:
        with open(batch, "r") as f:
            summaries.append(createPartitionedSummary(str(f.read())))
    #summary = stichSummaries(summaries)
    #print("Summary:\n------------\n" + summary)
    summary(summaries)
    notes(' '.join(summaries))
    practceProblems(' '.join(summaries))

    for batch in batches:
        os.remove(batch)
    



def practceProblems(summary):
    gpt_prompt = "Give me a few practice problems and an answer key for the problems based on the following summary:\n\n" + summary
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    with open("Practice_Problems.txt", "w") as f:
        f.write(response.choices[0].text)
    return response.choices[0].text

def notes(summary):
    gpt_prompt = "Give me a whole page's worth of nicely formatted notes, using proper spacing, titles, and bullet points based on the following summary:\n\n" + summary
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    with open("Notes.txt", "w") as f:
        f.write(response.choices[0].text)
    return response.choices[0].text

def summary(summaries):
    transcript = ""
    for summary in summaries:
        transcript += summary
    with open("Summary.txt", "w") as f:
        f.write(transcript)
    return transcript


def stichSummaries(summaries):
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

def createPartitionedSummary(partitionedTranscript):
    maxChar = math.floor(2000 / len(batches)) # 2000 is the safe amount for max character length
    gpt_prompt = "Give me a summary that has a hard max of " + str(maxChar) + """ characters, but try to  
                 "make it as detailed as possible for this transcript (don't mention that this is a transcript summary):\n\n""" + partitionedTranscript
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = gpt_prompt,
        temperature = 0.5,
        max_tokens = 1000
    )
    return response.choices[0].text

main()




