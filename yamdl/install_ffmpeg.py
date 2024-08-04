import platform
import subprocess
import sys


def install_ffmpeg():
    system = platform.system().lower()

    if system == 'windows':
        try:
            subprocess.run(['winget', 'install', '--id', 'ffmpeg'], check=True)
            print('ffmpeg has been installed using winget.')
        except subprocess.CalledProcessError:
            print('Failed to install ffmpeg using winget.')
            sys.exit(1)

    elif system == 'linux':
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', '-y', 'ffmpeg'], check=True)
        print('ffmpeg has been installed.')
    elif system == 'darwin':  # macOS
        subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
        print('ffmpeg has been installed.')
    else:
        print(f'Unsupported OS: {system}')
        sys.exit(1)


if __name__ == "__main__":
    install_ffmpeg()
