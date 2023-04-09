# 2023 Bitcamp[^1]

### Basic Premise:
The goal of the program is to quickly extract information from lecture videos. Whether it's notes, summaries of varying lengths and detail, or even practice problems with an answer key, students can use this program to save large amounts of time in parsing recordings of lectures. The user has the option to paste the transcript, upload an mp3 file, or paste in a Youtube link, then they'll be presented with several options on the kind of information they want to get. 

---

### Under the Hood:
If a user inputs a YouTube link, the program will use pytube to download the video as an mp3 file. Now, the mp3 file, whether obtained from a YouTube link or uploaded directly, is converted using OpenAI[^2]'s Whisper from audio to text. Then, the GPT API takes in the text and produces the formatted outputs for the user's convenience (summary, notes, practice problems). 

---

### How to Upload a Panopto[^3] Video:
1.  Go to the page of your desired panopto recording
2.  Open Developer Tools
3.  Look at the tabs at the top with names like “Elements”, “Console”, “Sources”, etc”
4.  Click on the tab that says “Network”
5.  Click on the filter text box and type in “mu38”
6.  Click on the first result that says “master.m3u8...”
7.  Under the General pane, copy the Request URL
8.  Now Open VLC Media Player
9.  Click on File -> Open Network
10. Paste the URL into the textbook 
11. Check the box at the bottom of the page that says stream output and click Settings
12. Specify an output directory and hit OK
13. Now when you’re returned to the previous page and hit Open. The file will stream and at the end you’ll have your file

---
### Setup:
`git clone https://github.com/RodzAmor/Bitcamp2023/LectureGPT.git` to copy down the project

`cd LectureGPT` to navigate into the project

`python LectureGPT.py` to start the GUI



[^1]: [Bitcamp](https://bit.camp/) is the 36 hour premier hackathon at the University of Maryland, and one of the largest on the entire East Coast. 
[^2]: [OpenAI's API](https://openai.com/blog/openai-api) allows easy access to AI models which are developed by OpenAI.
[^3]: [Panopto](https://www.panopto.com/) Panopto is a video platform, used by many higher educational facilities, typically where recordings of lectures are uploaded. ↩