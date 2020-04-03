import os
import json as json
import database_helper.directory_helper as directoryHelper
import models as model

defaultDirectory = "database"


def json_to_file(data, fileName, directoryName=defaultDirectory, ascii=True):
    dirPath = os.path.join("./", directoryName)
    fpath = os.path.join(dirPath, fileName + ".txt")

    if not directoryHelper.checkDir(dirPath):
        directoryHelper.createDir(directoryName)

    with open(fpath, "w") as outfile:
        if ascii:
            json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=True)
        else:
            json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=False)


def file_to_json(fileName, directoryName=defaultDirectory):
    dirPath = os.path.join("./", directoryName)
    fpath = os.path.join(dirPath, fileName + ".txt")
    data = None

    if not directoryHelper.checkDir(dirPath):
        print("Error: File in the path was not found -> {} ".format(fpath))
        return data

    try:
        with open(fpath) as infile:
            data = json.load(infile)
    except FileNotFoundError as e:
        print("Error: ", e)

    return data


def isfile(fileName, directoryName=defaultDirectory, debug=False):
    dirPath = os.path.join("./", directoryName)
    fpath = os.path.join(dirPath, fileName + ".txt")
    if os.path.exists(path=fpath):
        if debug:
            print("file exists")
        return True

    else:
        if debug:
            print("file does not exist")
        return False

# def update_user_info(newName: str=None, newTemp: int=None, newIsHome: bool=None):
#     if()
