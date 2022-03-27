from pytube import Playlist, YouTube
from tqdm import tqdm
import os

# for playlists:
playlist = Playlist('https://www.youtube.com/watch?v=YNB6aIwC8mg&list=PLrxByE8f6bAkMOm721jL91JxPPwDDmrsz&index=1')
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))


for video in tqdm(playlist.videos):
    try:
        video = video.streams.filter(only_audio=True).first()
        out_file = video.download()

        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
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