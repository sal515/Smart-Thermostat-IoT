import os
import json as json
import models as model
import databaseHelper.json_helpers.directory_helper as directoryHelper

from filelock import Timeout, FileLock

defaultDirectory = "storage"


def generate_dirPath_filePath(directoryName, fileName):
    fileName = fileName.replace("/", "_")
    dirPath = os.path.join("./", directoryName)
    fpath = os.path.join(dirPath, fileName + ".txt")
    return dirPath, fpath


def json_to_file(dataObjAsDict, fileName: str, directoryName=defaultDirectory, ascii=True):
    dirPath, fpath = generate_dirPath_filePath(directoryName, fileName)

    fLockPath = fpath + ".lock"
    lock = FileLock(fLockPath)

    with lock:
        # print("locked")
        if not directoryHelper.checkDir(dirPath):
            directoryHelper.createDir(directoryName)

        with open(fpath, "w") as outfile:
            if ascii:
                json.dump(dataObjAsDict, outfile, indent=4, sort_keys=True, ensure_ascii=True,
                          cls=model.encoder)
            else:
                json.dump(dataObjAsDict, outfile, indent=4, sort_keys=True, ensure_ascii=False, cls=model.encoder)


def file_to_json(fileName: str, directoryName=defaultDirectory):
    dirPath, fpath = generate_dirPath_filePath(directoryName, fileName)

    data = None

    if not directoryHelper.checkDir(dirPath):
        print("Error: File in the path was not found -> {} ".format(fpath))
        return data

    fLockPath = fpath + ".lock"
    lock = FileLock(fLockPath)

    with lock:

        try:
            with open(fpath) as infile:
                data = json.load(infile)
        except FileNotFoundError as e:
            print("Error: ", e)

    return data


def isfile(fileName: str, directoryName=defaultDirectory, debug=False):
    dirPath, fpath = generate_dirPath_filePath(directoryName, fileName)

    if os.path.exists(path=fpath):
        if debug:
            print("file exists")
        return True

    else:
        if debug:
            print("file does not exist")
        return False


if __name__ == '__main__':
    json_to_file({"dataObjAsDict": "a"}, "test")
    # print(fpath)
