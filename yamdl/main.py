import argparse
import os
import subprocess
import sys
import time

from converter import convert_audio
from downloader import download_audio


def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("ffmpeg is not installed or not found in PATH. Installing ffmpeg...")
        subprocess.check_call([sys.executable, 'install_ffmpeg.py'])
        # Re-check after installation
        try:
            subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("ffmpeg successfully installed.")
        except FileNotFoundError:
            print("ffmpeg installation failed. Please ensure ffmpeg is correctly installed.")
            sys.exit(1)


def get_music_download_directory(download_path):
    # Change the folder name to anything you want
    folder = "Yamdl"
    # Determine the download path and if it's None, default to user's music directory
    if download_path is None or download_path == '.':
        base_path = os.path.expanduser('~/Music')
        print("No Download Directory was specified!")
        time.sleep(2)
        print(f"Defaulting Downloads to this Folder: {base_path}")
        time.sleep(3)
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        base_path = os.path.join(download_path, folder)
        # Create the new folder if it doesn't already exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Folder: '{folder}' created successfully.")
        else:
            print(f"Folder: '{folder}' already exists.")

    return base_path


if __name__ == "__main__":
    # Check and install required dependencies
    check_and_install('yt_dlp')
    check_and_install('chardet')

    # Check if ffmpeg is installed
    check_ffmpeg()

    # Arguments for cli
    parser = argparse.ArgumentParser(description="Yamdl is a CLI utility to download Music from YouTube Videos")
    parser.add_argument('url', metavar='url', type=str, help="Enter the YouTube video URL")
    # Add the optional download directory argument
    parser.add_argument('-d', '--dir', metavar='dir', type=str, default=None,
                        help="Download directory (default is ~/Music)")

    args = parser.parse_args()
    url = args.url

    download_dir = args.dir
    # Pass the download directory to this function
    path = get_music_download_directory(download_dir)
    print(f"Download will now begin at this location: {os.path.abspath(path)}")

    # Download the audio file
    download_audio(url, path)

    # Convert all downloaded files to MP3
    for file_name in os.listdir(path):
        if file_name.endswith(('.webm', '.m4a', '.opus')):
            full_path = os.path.join(path, file_name)
            convert_audio(full_path, path)

    print(f"Audio has been downloaded and saved to {path}")
