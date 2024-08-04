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
        distro = None
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('ID='):
                        distro = line.strip().split('=')[1]
                        break
        except FileNotFoundError:
            print('Unable to determine Linux distribution.')
            sys.exit(1)

        if distro in ['ubuntu', 'debian']:
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'ffmpeg'], check=True)
            print('ffmpeg has been installed on Debian-based system.')
        elif distro in ['arch', 'manjaro']:
            subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm'], check=True)
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'ffmpeg'], check=True)
            print('ffmpeg has been installed on Arch-based system.')
        else:
            print(f'Unsupported Linux distribution: {distro}')
            sys.exit(1)
    elif system == 'darwin':  # macOS
        subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
        print('ffmpeg has been installed on macOS.')
    else:
        print(f'Unsupported OS: {system}')
        sys.exit(1)


if __name__ == "__main__":
    install_ffmpeg()
