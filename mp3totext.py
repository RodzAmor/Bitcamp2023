import os
import openai
import m3u8
import requests
import m3u8_To_MP4

file_name = 'Video 1'
file_path = './'

url_info = ''
url_cmp = 'index.m3u8'
url_1 = url_info + url_cmp

# "https://d2y36twrtb17ty.cloudfront.net/sessions/9ac3810b-fd31-4bdb-9b06-af660118e77a/6ce528a3-3ac9-4108-a38a-6b2983eb9351.screen.hls/master.m3u8?InvocationID=52a2c806-c2d5-ed11-a9ef-0a8e213f0382&tid=00000000-0000-0000-0000-000000000000&StreamID=6ce528a3-3ac9-4108-a38a-6b2983eb9351&ServerName=umd.hosted.panopto.com"
r_1 = requests.get("https://d2y36twrtb17ty.cloudfront.net/sessions/9ac3810b-fd31-4bdb-9b06-af660118e77a/6ce528a3-3ac9-4108-a38a-6b2983eb9351.screen.hls/master.m3u8?InvocationID=52a2c806-c2d5-ed11-a9ef-0a8e213f0382&tid=00000000-0000-0000-0000-000000000000&StreamID=6ce528a3-3ac9-4108-a38a-6b2983eb9351&ServerName=umd.hosted.panopto.com")

m3u8_master = m3u8.loads(r_1.text)

file_number = 0
i = 0
percentage = 0.0

for segment in m3u8_master.data['segments']:
    file_number += 1

print(file_number)

with open(file_path + file_name + '.ts', 'wb') as f:
    for segment in m3u8_master.data['segments']:
        url = url_info + segment['uri']
        while(True):
            try:
                r = requests.get(url,timeout = 15)
            except:
                continue
            break
        f.write(r.content)

# url = "https://d2y36twrtb17ty.cloudfront.net/sessions/9ac3810b-fd31-4bdb-9b06-af660118e77a/6ce528a3-3ac9-4108-a38a-6b2983eb9351.screen.hls/master.m3u8?InvocationID=52a2c806-c2d5-ed11-a9ef-0a8e213f0382&tid=00000000-0000-0000-0000-000000000000&StreamID=6ce528a3-3ac9-4108-a38a-6b2983eb9351&ServerName=umd.hosted.panopto.com"
# r = requests.get(url, allow_redirects=True)
# open('test.m3u8', 'wb').write(r.content)

# playlist = m3u8.load('test.m3u8')
# print(playlist.segments)
# print(playlist.dumps())

# openai.api_key = os.getenv("OPEN_API_KEY")

# Keep in mind the audiofile should be less than 25 mb
# audio_file = open("test.mp3", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript)

