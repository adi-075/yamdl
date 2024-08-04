import os
import subprocess
import sys

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
    # Check and install required packages
    check_and_install('yt_dlp')

    # Check if ffmpeg is installed
    check_ffmpeg()

    # Proceed with the user input
    url = input("Enter the URL of the video: ")

    # Check if the user wants to make a Music Directory in the cwd
    set_music_cwd = input("Do you want to Download in the Current Directory? [Y/n]").lower()
    if set_music_cwd == 'y':
        cwd = os.getcwd()
        folder = "Music"
        folder_path = os.path.join(cwd, folder)
        # Create the new folder if it doesn't already exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder: '{folder}' created successfully.")
        else:
            print(f"Folder: '{folder}' already exists.")
        download_path = os.path.join(os.getcwd(), 'Music')
    else:
        # Stores in the User Music Directory
        download_path = os.path.expanduser('~/Music')

    # Download the audio file
    download_audio(url, download_path)

    # Convert all downloaded files to MP3
    for file_name in os.listdir(download_path):
        if file_name.endswith(('.webm', '.m4a', '.opus')):
            full_path = os.path.join(download_path, file_name)
            convert_audio(full_path, download_path)

    print(f"Audio has been downloaded and saved to {download_path}")
