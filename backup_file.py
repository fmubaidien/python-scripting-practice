import os

<<<<<<< Updated upstream
OG_DIR_PATH="/home/deck/work/python-scripting-practice/test" #change
BK_FILE_PATH="test.tar.gz" #change


def copy_file(): 
    os.system(f'tar -zvcf {BK_FILE_PATH} -C {OG_DIR_PATH} .')

def test_compress():
    if os.system(f'gzip -t {BK_FILE_PATH}') == 0:
        print(f'File compressed successfully\n')
    else:
        print(f'Error file did not compress successfully\n')

copy_file()
test_compress()
=======
OG_DIR_PATH="/home/faisal/temp/test/" #change
BK_FILE_PATH="test.tar.gz" #change


def create_backup(): 
    sys_output = os.system(f'tar -zvcf {BK_FILE_PATH} -C {OG_DIR_PATH} .')

def verify_backup():
    

create_backup()
>>>>>>> Stashed changes
