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


if __name__ == "__main__":
    # Check and install required python packages
    check_and_install('yt_dlp')

    # Check if ffmpeg is installed
    check_ffmpeg()

    # Proceed with the user input
    url = input("Enter the URL of the video: ")

    # Set custom download path here
    download_path = None

    # Saves the Music to your Music Directory
    if download_path is None:
        download_path = os.path.expanduser('~/Music')

        print("No Download Directory was specified!")
        time.sleep(2)

        print(f"Defaulting Downloads to this Folder:{download_path}")
        time.sleep(3)

        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        folder = "Music"
        folder_path = os.path.join(download_path, folder)
        # Create the new folder if it doesn't already exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder: '{folder}' created successfully.")
        else:
            print(f"Folder: '{folder}' already exists.")
        download_path = os.path.join(download_path, folder)

    # Download the audio file
    print(os.path.abspath(download_path))
    download_audio(url, download_path)

    # Convert all downloaded files to MP3
    for file_name in os.listdir(download_path):
        if file_name.endswith(('.webm', '.m4a', '.opus')):
            full_path = os.path.join(download_path, file_name)
            convert_audio(full_path, download_path)

    print(f"Audio has been downloaded and saved to {download_path}")
