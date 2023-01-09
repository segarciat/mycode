#!/usr/bin/env python3

import shutil
import os

def main():
    # Change the current working directory.
    os.chdir('/home/student/mycode/tutorials/lab55-move-rename-files/')

    # Move the raynor file to the ceph_storage folder
    shutil.move('raynor.obj', 'ceph_storage/')

    # Prompt user for a new name for kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')

    # Rename kerrigan.obj file based on user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == '__main__':
    main()
