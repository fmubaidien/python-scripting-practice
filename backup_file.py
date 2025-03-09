import os

OG_DIR_PATH="/home/faisal/temp/test" #change
BK_FILE_PATH="test.tar" #change


def copy_file(): 
    os.system(f'tar -zvcf {BK_FILE_PATH} -f {BK_DIR_PATH}')


copy_file()
