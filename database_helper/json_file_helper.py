import os
import json as json
import database_helper.directory_helper as directoryHelper
import models as model

defaultDirectory = "database"


def generate_dirPath_filePath(directoryName, topicName):
    fileName = topicName.replace("/", "_")
    dirPath = os.path.join("./", directoryName)
    fpath = os.path.join(dirPath, fileName + ".txt")
    return dirPath, fpath


def json_to_file(dataObjAsDict, topicName: str, directoryName=defaultDirectory, ascii=True):
    dirPath, fpath = generate_dirPath_filePath(directoryName, topicName)

    if not directoryHelper.checkDir(dirPath):
        directoryHelper.createDir(directoryName)

    with open(fpath, "w") as outfile:
        if ascii:
            json.dump(dataObjAsDict, outfile, indent=4, sort_keys=True, ensure_ascii=True)
        else:
            json.dump(dataObjAsDict, outfile, indent=4, sort_keys=True, ensure_ascii=False)


def file_to_json(topicName: str, directoryName=defaultDirectory):
    dirPath, fpath = generate_dirPath_filePath(directoryName, topicName)

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


def isfile(topicName: str, directoryName=defaultDirectory, debug=False):
    dirPath, fpath = generate_dirPath_filePath(directoryName, topicName)

    if os.path.exists(path=fpath):
        if debug:
            print("file exists")
        return True

    else:
        if debug:
            print("file does not exist")
        return False
