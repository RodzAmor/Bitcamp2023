# importing the module 
from pytube import YouTube 

# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=adh7OhA0UFI"

try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 

yt.streams.filter(file_extension='mp4').order_by('resolution').first().download(filename="temp.mp4")