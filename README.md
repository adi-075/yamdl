# Yet Another Music Downloader (yamdl)

Ever wondered where those .mp3 files we used to download disappeared? The reason is streaming services ended the downloads of .mp3 files.

This Simple Python project aims to download High-Quality Audio from YouTube videos and convert them to MP3 format so you have a backup for yourself.

You will never need those creepy & malicious websites to download .mp3 files ever again.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/adi-075/yamdl.git
    cd yamdl
    ```

2. **Install required Python Dependencies:**

    ```
   The required dependencies are auto-installed by the program.
   ```

3. **Installing ffmpeg:**

    `ffmpeg` is necessary for audio conversion. The `install_ffmpeg.py` script will handle this automatically if `ffmpeg` is not found.

## Usage

You can use the `main.py` script to download and convert audio. The script defaults the music download to the User's Music Directory but it can be saved to any directory you want with an optional argument --dir.
### Example



```python
python main.py -h
usage: main.py [-h] [-d dir] url

Yamdl is a CLI utility to download Music from YouTube Videos

positional arguments:
  url                Enter the YouTube video URL

options:
  -h, --help         show this help message and exit
  -d dir, --dir dir  Download directory (default is ~/Music)

```

It takes a positional argument url to download the music<br>
You can optionally change the download directory using ``-d`` argument


## Project Structure

- `converter.py`: Contains the logic for converting downloaded audio files to MP3 format.
- `downloader.py`: Handles downloading audio from YouTube using `yt-dlp`.
- `install_ffmpeg.py`: Installs `ffmpeg` on your system if it is not already installed.
- `main.py`: The main script that ties everything together, handling command-line arguments, checking for required dependencies, and invoking the download and conversion processes.
