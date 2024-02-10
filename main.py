# from dirsync import sync
import os
import glob
# import zipfile
import shutil
import time
from shutil import copy2
from itertools import repeat


ParentFile = ''
extDisk = ''
# trash = '~/.Trash'

folders = []
movedFolders = []

def selectTransferalPath():
    global ParentFile
    global extDisk
    ParentFile = str(input("What is the parent file? (Paste File Path)"))
    extDisk = str(input("Where do you want to transfer to? (Paste File Path)"))
    print("Parent file is ", ParentFile)
    print("Your transfering to ", extDisk)
    return 

def ProjectFinder():
    LogicFilesPath = '/Users/sanjith/Music/Logic/ProjectBank/*.logicx'
    # dirs = os.listdir(LogicFilesPath)
    # print(dirs)
    filterLogicFiles = glob.glob(LogicFilesPath)
    # print(filterLogicFiles)
    dirs = os.listdir(ParentFile)
    # print(dirs)
    for i in dirs:
        i = os.path.join(ParentFile, i)
        if i in filterLogicFiles:
            None
        else:
            last_modified_date = os.path.getmtime(i)
            currentTime = time.time()
            x = currentTime - last_modified_date
            # print(last_modified_date)
            # print(currentTime)
            if x < 604800.00:
                print('{} does not need to be transfered'.format(i))
                # time.sleep(3)
            else:
                folders.append(i)
                # print('{} has been collected.'.format(i))
                # time.sleep(3)
    return 

def fileException():
    if folders == []:
        print('No Files To Be Transfered!')
    else:
        global fileIgnore
        print('Here are the files we have collected: {}'.format(folders))
        fileIgnore = input("Do you want to keep any projects (paste file path) If not, type 'n'\n")
        if fileIgnore == 'n':
            None
        else:
            #  work on quotation exception below
            fileIgnore.replace("'","",-1)
        fileInclude = input("Want to transfer more? (paste file path) If not, type 'n' \n")
        if fileInclude == 'n':
            None
        else:
            fileInclude.replace("'","")
            FilesIncluded = fileInclude.split(' /')
            for i in FilesIncluded[1:]:
                comb = ['/', i]
                comb1 = "".join(comb)
                FilesIncluded.append(comb1)
                FilesIncluded.remove(i)
            for i in FilesIncluded:
                print(i)
                folders.append(i)
    return


def moveFile():
    for i in folders:
        if i.endswith('.DS_Store'):
            print('We have ignored the ds_store file')
            # time.sleep(3)
            None
        elif i == fileIgnore:
            print('{} has been ignored'.format(i)) 
            # time.sleep(3)
            None
        else:
            try:
                movedFile = shutil.move(i, extDisk, copy_function=copy2)
                movedFolders.append(movedFile)
                print('{} has been moved'.format(i))
            except Exception as e:
                print(e)
            # time.sleep(3)

def undo():
    undobutton = (input('If you want to undo what you did press 2. If you want to end program, press 1'))
    if undobutton == 1:  
        return
    elif undobutton == 2:
        for i in movedFolders:
            shutil.move(i, ParentFile, copy_function=copy2)
            print('{} has been moved back'.format(i))
    else:
        print('You did not type 1 or 2!!')
        repeat(undo())

def main():
    selectTransferalPath()
    ProjectFinder()
    fileException()
    moveFile()
    undo()

main()


