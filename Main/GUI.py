from tkinter import *
from tkinter import filedialog
from dotenv import load_dotenv
import customtkinter as ct
import os
import openai
from PIL import Image
# import threading

# Set up the environment
load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

ct.set_appearance_mode("light")
window = ct.CTk()

FILE_PATH = None
RAW_TRANSCRIPT = None
YOUTUBE_URL = None
OPTION = -1

# Window Size
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

def browseFiles():
    filePath = filedialog.askopenfilename(initialdir="./",
                                          title="Select a file",
                                          filetypes=(("Mp3 Files", "*.mp3"),
                                                     ("MP4 files", "*.mp3")))
    print(filePath)
    fileNameLabel.configure(text=filePath)

def validateInput():
    # The number of input should not exceed 1
    inputs = 0

    if(fileNameLabel.cget("text") != "File Path"):
        inputs += 1
    if(textBox.get("1.0", END) != "\n"):
        inputs += 1
    if(youtubeTextBox.get("1.0", END) != "\n"):
        inputs += 1

    if(inputs > 1):
        print("A")
        validateLabel.configure(text="You can only submit one input at a time!")
        return
    elif(inputs == 1):
        print("B")
        validateLabel.configure(text="")
        
        if(fileNameLabel.cget("text") != "File Path"):
            OPTION = 0
            FILE_PATH = fileNameLabel.cget("text")
        if(textBox.get("1.0", END) != "\n"):
            OPTION = 1
            RAW_TRANSCRIPT = textBox.get("1.0", END)
        if(youtubeTextBox.get("1.0", END) != "\n"):
            OPTION = 2
            YOUTUBE_URL = youtubeTextBox.get("1.0", END)
        
        # Delete the widgetsÇ
        for widgets in window.winfo_children():
            widgets.destroy()
        
        createNewScreen()

def createNewScreen():
    # Modify the commands to the corresponding method
    summaryButton = ct.CTkButton(window, text="Summary", width=250, height=60, font=ct.CTkFont(family="Helvetica", size=20, weight="bold"), command=validateInput)
    notesButton = ct.CTkButton(window, text="Notes", width=250, height=60, font=ct.CTkFont(family="Helvetica", size=20, weight="bold"), command=validateInput)
    practiceButton = ct.CTkButton(window, text="Practice Problems", width=250, height=60, font=ct.CTkFont(family="Helvetica", size=20, weight="bold"), command=validateInput)

    ouputLabel = ct.CTkLabel(window, text="Output", font=ct.CTkFont(family="Helvetica", size=30, weight="bold"))
    outputTextBox = ct.CTkTextbox(window, width=500, height=500)

    summaryButton.place(relx=0.2, rely=0.3)
    notesButton.place(relx=0.2, rely=0.5)
    practiceButton.place(relx=0.2, rely=0.7)

    outputTextBox.place(relx=0.5, rely=0.2)
    ouputLabel.place(in_=outputTextBox, relx=0.5, rely=0.0, y=-80, anchor="n")

    # Make the logic
    # outputTextBox.configure(text=[The output you want to show])


title = ct.CTkLabel(window, text="Welcome to LectureGPT", font=ct.CTkFont(family="Helvetica", size=40, weight="bold"))
instructions = ct.CTkLabel(window, text="Choose your input", font=ct.CTkFont(family="Helvetica", size=20, weight="bold"))
submitButton = ct.CTkButton(window, text="Submit", width=200, height=40, font=ct.CTkFont(family="Helvetica", size=30, weight="bold"), command=validateInput)
validateLabel = ct.CTkLabel(window, text="", font=ct.CTkFont(family="Helvetica", size=15), text_color="red")

fileFrame = ct.CTkFrame(window, width=300, height=200, corner_radius=20)
browseFileButton = ct.CTkButton(fileFrame, text="Browse Files", command=browseFiles)
fileLabel = ct.CTkLabel(fileFrame, text="MP3/MP4 File", font=ct.CTkFont(family="Helvetica", size=20, weight="bold"))
fileNameLabel = ct.CTkLabel(fileFrame, text="File Path", font=ct.CTkFont(family="Helvetica", size=15))

textFrame = ct.CTkFrame(window, width=350, height=350, corner_radius=20)
textBox = ct.CTkTextbox(textFrame, width=300, height=200)
textBoxLabel = ct.CTkLabel(textFrame, text="Paste Lecture Text", font=ct.CTkFont(family="Helvetica", size=20, weight="bold"))

linkFrame = ct.CTkFrame(window, width=300, height=200, corner_radius=20)
youtubeTextBox = ct.CTkTextbox(linkFrame, width=200, height=10)
youtubeLabel = ct.CTkLabel(linkFrame, text="Youtube Link", font=ct.CTkFont(family="Helvetica", size=20, weight="bold"))
youtubeIcon = ct.CTkLabel(linkFrame, text="", image=ct.CTkImage(light_image=Image.open("./youtube.ico"), size=(50, 50)))

title.place(relx=0.5, rely=0.12, anchor=CENTER)
instructions.place(relx=0.5, rely=0.22, anchor=CENTER)
submitButton.place(relx=0.5, rely=0.87, anchor=CENTER)
validateLabel.place(relx=0.5, rely=0.94, anchor=CENTER)

fileFrame.place(relx=0.2, rely=0.55, anchor=CENTER)
fileLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
browseFileButton.place(relx=0.5, rely=0.5, anchor=CENTER)
fileNameLabel.place(relx=0.5, rely=0.8, anchor=CENTER)

textFrame.place(relx=0.5, rely=0.55, anchor=CENTER)
textBoxLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
textBox.place(relx=0.5, rely=0.6, anchor=CENTER)

linkFrame.place(relx=0.8, rely=0.55, anchor=CENTER)
youtubeLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
youtubeTextBox.place(relx=0.5, rely=0.5, anchor=CENTER)
youtubeIcon.place(relx=0.5, rely=0.8, anchor=CENTER)

window.mainloop()
