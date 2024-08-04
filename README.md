# Yet Another Music Downloader (yamdl)

Ever wondered where those .mp3 files we used to download disappeared? The reason is streaming services ended the downloads of .mp3 files.

This Simple Python project aims to download High-Quality Audio from YouTube videos and convert them to MP3 format so you have a backup for yourself.

You will never need those creepy & malicious websites to download .mp3 files ever again.

## Project Structure

- `converter.py`: Contains the logic for converting downloaded audio files to MP3 format.
- `downloader.py`: Handles downloading audio from YouTube using `yt-dlp`.
- `install_ffmpeg.py`: Installs `ffmpeg` on your system if it is not already installed.
- `main.py`: The main script that ties everything together, handling command-line arguments, checking for required dependencies, and invoking the download and conversion processes.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/adi-075/yamdl.git
    cd yamdl
    ```

2. **Install required Python packages:**

    ```sh
    pip install yt-dlp
    ```

3. **Installing ffmpeg:**

    `ffmpeg` is necessary for audio conversion. The `install_ffmpeg.py` script will handle this automatically if `ffmpeg` is not found.

## Usage

You can use the `main.py` script to download and convert audio. The script accepts command-line arguments for the YouTube video URL and optionally the directory where the audio files should be saved.

### Example

To download audio from a YouTube video and save it to a specified directory:

```python
python main.py 
Enter the URL of the video: "https://youtube.com/somevideourl"
```