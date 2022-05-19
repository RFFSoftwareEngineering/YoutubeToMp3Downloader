from __future__ import unicode_literals
from pytube import Playlist, YouTube
from tqdm import tqdm
import os
import time
import youtube_dl


# for playlists:

playlist = Playlist('https://www.youtube.com/playlist?list=PLrxByE8f6bAkMOm721jL91JxPPwDDmrsz')
print('Number Of Videos In playlist: %s' % len(playlist.video_urls[:12]))

lista = []
f = open('url.txt', 'w+')
for item in playlist.video_urls[:14]:
    f.write(f"{item}\n")
    lista.append(item)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [my_hook],  
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(lista)

"""
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLrxByE8f6bAkMOm721jL91JxPPwDDmrsz'])

"""
"""
x = 0.0

for video in tqdm(playlist.videos[:14]):
    try:
        video = video.streams.filter(only_audio=True).first()
        out_file = video.download()
        print(out_file)

        base, ext = os.path.splitext(out_file)
        print(base)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        time.sleep(x)
        if x == 30:
            x = 30 - 25
        else:
            x += 0.015
        print(video)
    except:
        pass

print("Done!")
"""
# for single song:
#video = YouTube('https://www.youtube.com/watch?v=8nFo7eHDppQ')
#video = video.streams.filter(only_audio=True).first()
#out_file = video.download()
#base, ext = os.path.splitext(out_file)
#new_file = base + ".mp3"
#os.rename(out_file, new_file)
