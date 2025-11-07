import subprocess
import sys

def install_packages():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

install_packages()