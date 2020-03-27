import database_helper as db
import models as model

# Directory names
databaseDirectoryName = "database"
# Data file names
topicsJson = "topics.txt"
subscribersJson = "subscribers.txt"
publishersJson = "publishers.txt"


# Directory creation tests
# db.createDir(databaseDirectoryName)
# db.removeDir(databaseDirectoryName)
# db.createDir(databaseDirectoryName)

# File creation tests
# example_data = dict(param1="hello", param2="yes", param3=[dict(_inner_param=1)], param4=dict())
# db.json_to_file(example_data, subscribersJson, databaseDirectoryName)
# db.json_to_file(example_data, topicsJson, databaseDirectoryName)
# db.json_to_file(example_data, publishersJson, databaseDirectoryName)

# File reading tests
# a = db.file_to_json(publishersJson, databaseDirectoryName)
# print(a)


# Conversions between dict and object test
# tim = model.userInfo("Tim", 19, False)
# hancock = model.userInfo("Hancock", 24, True)
# plo = model.userInfo("Plo", 21, True)
#
# print(tim.asDict()["name"])
# print(model.asUserInfo(tim.asDict()))
# print(tim)

