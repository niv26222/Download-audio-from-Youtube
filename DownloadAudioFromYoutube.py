# Python program to Download audio from Youtube


from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar','16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

with youtube_dl.youtube_DL(ydl_opts) as ydl:
    ydl.Download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

 