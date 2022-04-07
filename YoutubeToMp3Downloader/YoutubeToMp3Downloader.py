from pytube import Playlist, YouTube
from tqdm import tqdm
import os
import time


# for playlists:
playlist = Playlist('https://www.youtube.com/watch?v=-P6yJjuDbas&list=PLrxByE8f6bAkMOm721jL91JxPPwDDmrsz&index=1')
print('Number Of Videos In playlist: %s' % len(playlist.video_urls[:9]))


x = 0.0


for video in tqdm(playlist.videos[:9]):
    try:
        video = video.streams.filter(only_audio=True).first()
        out_file = video.download()

        base, ext = os.path.splitext(out_file)
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


# for single song:
"""
video = YouTube('https://www.youtube.com/watch?v=FTB1b228h8g')
video = video.streams.filter(only_audio=True).first()
out_file = video.download()
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)
"""