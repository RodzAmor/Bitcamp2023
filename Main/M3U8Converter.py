# Converts m3u8 playlists to mp4. 
# m3u8 playlists usually obtained when trying to download video live streams. They are not fully understood by many players, and also they become completely unusable when they are moved from one directory to another. 
# This script can fix that issue by updating the m3u8 playlist file and converting it to mp4. 
# 
# It uses ffmpeg internally, so make sure to install ffmpeg before running this script. 
# Refer to this link for installation: https://ffmpeg.org/download.html
# 
# To run this scrpt, copy it to the directory containing the m3u8 file and run it from terminal using the command
# `python3 m3u8-converter.py`


import os
import shutil

OUTPUT_PATH = 'out' # Directory to move converted mp4 files
COMPLETED_PATH = 'completed' # Directory to move converted m3u8 and corresponding contents files


# Get all m3u8 files
def __list_m3u8_files():
    files = []
    for _ in os.listdir('.'):
        if _.endswith('.m3u8'):
            print('Found ' + _)
            files.append(_)
    return files


# Update the file path in the m3u8 playlist
def __rewrite_file_paths(f):
    print('Processing ' + f)
    file_contents = open(f).read()
    lines = file_contents.split('\n')
    new_lines = []
    for line in lines:
        if line.startswith('file://'):
            new_line = 'file://' + os.path.join(os.getcwd(), os.path.sep.join(line.split('/')[-2:]))
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    open(f, 'w').write('\n'.join(new_lines))


# Run the ffmpeg command to convert the file
def __covert_m3u8_file_to_mp4(f): 
    command = ''.join(['ffmpeg -allowed_extensions ALL -i "', f, '" -c:v copy -c:a copy -f mp4 "out/', f.replace('.m3u8', '.mp4'), '"'])
    print('Running command "' + command + '"')
    os.system(command)


# Utility to create necessary folders
def __make_dir(directory_name):
    if not os.path.exists(directory_name) and not os.path.isdir(directory_name):
        os.mkdir(directory_name)


# Move completed m3u8 file and the contents directory to completed
def __move_completed_file(f):
    shutil.move(f, os.path.join(COMPLETED_PATH, f))
    shutil.move(f.replace('.m3u8', '.m3u8_contents'), \
        os.path.join(COMPLETED_PATH, f.replace('.m3u8', '.m3u8_contents')))


# Perform the conversion for all files in the current directory
def convert_m3u8_files():
    files = __list_m3u8_files()
    
    __make_dir(OUTPUT_PATH)
    __make_dir(COMPLETED_PATH)

    print('\n\nProcessing files...')

    for f in files:
        __rewrite_file_paths(f)
        __covert_m3u8_file_to_mp4(f)
        __move_completed_file(f)


# Start the conversion
if __name__ == "__main__":
    convert_m3u8_files()
