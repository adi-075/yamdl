import os

from yt_dlp import YoutubeDL


def download_audio(url, download_path='music'):
    os.makedirs(download_path, exist_ok=True)

    ytdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(ytdl_opts) as ydl:
        ydl.download([url])
