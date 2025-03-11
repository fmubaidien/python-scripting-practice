import os

IP_LIST="test_ips"

def ping_server(server_ip):
    return os.system(f'ping -c 1 -w 10 {server_ip} > /dev/null')

def main():
    file = open(IP_LIST)
    lines = file.readlines()
    file.close()
    
    for line in lines:
        line = line.replace('\n','')
        if ping_server(line) == 0:
            print(f'{line} is online')
        else:
            print(f'{line} is offline')
    


main()