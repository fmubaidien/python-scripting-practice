import os

IP_LIST="test.ips"

def ping_server(server_ip):
    return os.system(f'ping {server_ip}')

def main():
    file = open(IP_LIST)
    lines = file.readlines()

    for line in lines:
        line = line.replace('\n','')
        if ping_server(line) == 0:
            print(f'{line} is online')
        else:
            print(f'{line} is offline')
    
    file.close()

main()