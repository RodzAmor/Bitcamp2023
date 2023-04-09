from pytube import YouTube 
import os
from moviepy.editor import *

def convert_youtube_link(link):
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(link) 
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="")
        new_file = "Youtube_Video" + ".mp3"
        os.rename(out_file, new_file)

    except Exception as e: 
        print("Error during conversion:", e)