import os
import subprocess


# Convert the downloaded file into an mp3 file
def convert_audio(source_file, target_path):
    target_file = os.path.join(target_path, os.path.splitext(os.path.basename(source_file))[0] + '.mp3')
    command = ['ffmpeg', '-i', source_file, '-vn', '-ar', '44100', '-ac', '2', '-b:a', '192k', target_file]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return None
    os.remove(source_file)
    return target_file