import os

OG_DIR_PATH="/home/faisal/temp/test" #change
BK_DIR_PATH="test.tar" #change


def copy_file(): 
    os.system(f'tar -zvcf {OG_DIR_PATH} -f {BK_DIR_PATH}')


copy_file()