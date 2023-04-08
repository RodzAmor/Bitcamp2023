# 2023 Bitcamp[^1]

### Basic Premise:
The goal of the program is to quickly extract information from any educational video or Panopto[^2] lecture recording. Whether it's notes, summaries of varying lengths and detail, or even practice problems with an answer key, students can use this program to save large amounts of time in parsing recordings of lectures. The user has the option to paste the transcript, upload an mp3 or mp4 file, or paste in a Youtube link, then they'll be presented with several options on the kind of information they want to get. 

---

### Under the Hood:
After a user inputs a URL link, the program will scrape the website to download the recording, extract the audio file from the recording, produce a transcript from converting the audio to text, then using the GPT[^3] API to produce the formatted outputs for the user's convenience. 

---

### Setup:
`git clone https://github.com/RodzAmor/Bitcamp2023/LectureGPT.git` to copy down the project
`cd LectureGPT` to navigate into the project



[^1]: [Bitcamp](https://bit.camp/) is the 36 hour premier hackathon at the University of Maryland, and one of the largest on the entire East Coast. 
[^2]: [Panopto](https://www.panopto.com/) is a video platform, used by many higher educational facilities, typically where recordings of lectures are uploaded.
[^3]: [OpenAI's API](https://openai.com/blog/openai-api) allows easy access to AI models which are developed by OpenAI.
