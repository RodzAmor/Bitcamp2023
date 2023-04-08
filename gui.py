from tkinter import *
from tkinter import filedialog
from dotenv import load_dotenv
import os
import openai
import json
# import threading

# Set up the environment
load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")
window = Tk()

# Window Size
# window.geometry("1000x1000")
# Full Screen
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
# Window Background
window.config(background = "white")

open_file = Label(window, text = "File Explorer", width = 100, height = 4, fg = "blue")
open_file.grid(column = 1, row = 1)

def browseFiles():
    filePath = filedialog.askopenfilename(initialdir="./",
                                          title="Select a file",
                                          filetypes=(("Mp3 Files", "*.mp3"),
                                                     ("MP4 files", "*.mp3")))
    print(filePath)
    
    # Different for Windows and Linux
    audio_file = open(filePath, "rb")

    transcript = str(openai.Audio.transcribe("whisper-1", audio_file))
    var.set(json.loads(transcript)["text"])
    audio_file.close()

button_explore = Button(window, text="Browse Files", command=browseFiles)

open_file = Label(window, text = "File Explorer", width = 100, height = 4)
open_file.grid(column = 1, row = 1)

var = StringVar()
transcript = Message(window, textvariable=var, width= 100, relief=RAISED)
var.set("Output")

button_explore.grid(column = 1, row = 2)
transcript.grid(column = 1, row = 3)

window.mainloop()