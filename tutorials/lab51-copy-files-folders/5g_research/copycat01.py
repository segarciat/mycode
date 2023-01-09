#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

def main():
    # move into the working directory
    os.chdir("/home/student/mycode/tutorials/lab51-copy-files-folders/")
    
    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    # copy the entire directoryA to directoryB
    relative_directory_path = "5g_research_backup/"
    if not os.path.exists(f"{relative_directory_path}"):
        shutil.copytree("5g_research/", relative_directory_path)
    
if __name__ == '__main__':
    main()
