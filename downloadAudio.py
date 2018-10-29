import youtube_dl

FORMAT = "mp3"

options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': u'%(title)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'quiet':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': FORMAT,
        'preferredquality': '192',
    }]
}

from os import rename
video_id = "cIriwVhRPVA"
video_id = input("[ID] Download video: ")
video_url = "https://www.youtube.com/watch?v=" + video_id

print("[INFO] Preparing to download")
with youtube_dl.YoutubeDL(options) as ydl:
    print("[INFO] Downloading...")
    ydl.download([video_url])
    print("[INFO] Processing download")
print("[INFO] Finished download")