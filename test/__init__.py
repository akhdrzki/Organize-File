import shutil 
import os

def sort_file(source, destination, file_format):
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        print("lol")

        if os.path.isfile(source_path) and any(filename.lower().endswith(ext) for ext in file_format):
            dest_path = os.path.join(destination, filename)
            shutil.move(source_path, dest_path)
            print('Moved Successfully')
        else: 
            print('there is no file to sort')


# Manipulate these section with your path directory

source = '/home/rizvii/Downloads/'
# image format such .jpg .png .gif .jpeg
dest_img = '/home/rizvii/Pictures/'
img_file = (".jpg", ".png", ".gif")

# document format such .docx, .csv, .ppt
dest_docs = '/home/rizvii/Documents/'
docs_file = (".hbs", ".csv", ".docx", "txt")

# archive format such .zip .rar 
dest_archive = '/home/rizvii/Archive/'
archive_file = (".zip", ".rar", ".pkg")

# desktop format such .exe, .msi etc
dest_desktop = '/home/rizvii/Desktop/'
desktop_file = (".desktop", ".msi", ".exe")

# video format such .mp4, mkv
dest_video = '/home/rizvii/Videos/'
video_file = ("mkv", "mp4")

# audio format such .mp3 .ma4
dest_audio = '/home/rizvii/Music/'
audio_file = (".mp3", ".ma4")

sort_file(source, dest_img, img_file)
sort_file(source, dest_docs, docs_file)
sort_file(source, dest_archive, archive_file)
sort_file(source, dest_desktop, desktop_file)
sort_file(source, dest_video, video_file)





