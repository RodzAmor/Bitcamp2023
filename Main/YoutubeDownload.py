from pytube import YouTube 

def convert_youtube_link(link):
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(link) 
        yt.streams.filter(file_extension='mp3').order_by('resolution').first().download(filename="Youtube_Video.mp3")
    except: 
        print("Connection Error") #to handle exception 

