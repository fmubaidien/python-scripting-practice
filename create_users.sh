#given a file that contains lines with an ip address a user name, a public key file path for the user name
#write a script to create the user in the server

list_file = "list.txt"

import os

def create_user(ip, username, path):
    ssh_filename = path.split('/')[-1]
    os.system(f'ssh {ip} "useradd {username} -m -s /bin/bash"')
    os.system(f'ssh {ip} "mkdir -p /home/{username}/.ssh"')
    os.system(f'scp {path} myuser@{ip}:/home/{username}/.ssh')
    os.system(f'ssh {ip} "mv /home/{username}/.ssh/{ssh_filename} /home/{username}/.ssh/authorized_keys"')
    os.system(f'ssh {ip} "chown -R {username}:{username} /home/{username}"')
    os.system(f'ssh {ip} "chmod -R 700 /home/{username}"')
    if os.system(f'ssh {ip} \"grep -q '^AllowUsers' /etc/ssh/sshd_config\"') == 0:
        os.system(f"ssh {ip} \"sed -i '/^AllowUsers/ s/$/ {username}/' /etc/ssh/sshd_config\"")
    else:
        os.system(f"ssh {ip} \"echo 'AllowUsers {username}' >> /etc/ssh/sshd_config\"")
    os.system(f'ssh {ip} "systemctl restart sshd"')
    


def main():
    with open(list_file, "r") as file:
        for line in file:
            line = line.strip().split()
            create_user(line[0],line[1],line[2])



main()