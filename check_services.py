import os

SER="alsa-restore.service"

def main():
    status = os.system(f'systemctl is-active {SER}')
    print(f'status is {status}')
main()