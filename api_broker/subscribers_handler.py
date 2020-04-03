import database_helper as dbHelper
import models as models

import json as json

# userInfo = models.deviceInfo(1, "000.000.000.000", "http://127.0.0.1:2000/")
topic = "data/user_preference"
# data = dict(userInfo=userInfo.asDict(), topic=topic)

# data = dict(dict(subscribers=[], publishers=[], messages=[]), topic=topic)
data = dict(models.topic(topic).asDict(), topic=topic)
dbHelper.json_to_file(data=data, fileName=data["topic"].replace("/", "_"))

topic_dictionary = dbHelper.file_to_json(fileName=data["topic"].replace("/", "_"))
topic_object = models.asTopic(topic_dictionary)

# def test():
#     dbHelper.json_to_file(data=data, fileName=topic.replace("/", "_"))
