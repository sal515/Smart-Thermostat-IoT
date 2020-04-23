# create file
# read file
# write to file
# delete file


# create directory
# remove directory
# move one directory up
# rename directory
# check if directory exists

import os


def currentDir():
    return os.getcwd()


def moveToPreviousDir():
    os.chdir("..")


def createDir(dirName):
    dir = os.path.join("./", dirName)
    if not os.path.exists(dir):
        os.mkdir(dir)


def removeDir(dirName):
    dir = os.path.join("./", dirName)
    if os.path.exists(dir):
        os.rmdir(dir)


def renameDir(oldDirName, newDirName):
    oldPath = os.path.join("./", oldDirName)
    newPath = os.path.join("./", newDirName)
    if os.path.exists(oldPath):
        os.rename(oldPath, newPath)


def checkDir(path):
    path = os.path.join(path)
    if os.path.exists(path) and os.path.isdir(path):
        return True

# Traversing directories
# rootdir = "c:\\temp"
# for root, dirs, files in os.walk(rootdir):
#     print("{0} has {1} files".format(root, len(files)))
