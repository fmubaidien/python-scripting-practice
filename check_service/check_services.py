import os

SER="firewalld"

def main():
    status = os.system(f'systemctl is-active {SER} > /dev/null')
    if status == 0:
        print(f'{SER} is active')
    else:
        print(f'{SER} is inactive')    
main()