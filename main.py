#!"C:\Python\python.exe"

from scripts.sort_file import sort_file  


### Here you must change the path as yours ###

source = "/home/rizvii/Downloads/"

# Image file 
dest_img = "/home/rizvii/Pictures/"
img_file = (".png", ".jpg", ".jpeg")


# Doc file 
dest_docs = ""
doc_file = ("", "")


# Archive file
dest_archive = ""
archive_file = ("", "")


# Audio file
dest_audio = ""
audio_file = ("", "")


# Video file
dest_video = ""
video_file = ("", "")



sort_file(source, dest_img, img_file) #img
sort_file(source, dest_docs, doc_file) #doc
sort_file(source, dest_archive, archive_file) #archive
sort_file(source, dest_audio, audio_file) #audio
sort_file(source, dest_video, video_file) #video

