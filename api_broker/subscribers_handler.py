import database_helper as dbHelper
import models as models
import json as json


def registerSubscriber(deviceInfo: models.deviceInfo, topic: str):
    if not dbHelper.isfile(topic):
        data = dict(models.topic(topic).asDict(), topic=topic)
        dbHelper.json_to_file(dataObjAsDict=data, topicName=topic)

    topic_dictionary = dbHelper.file_to_json(topic)
    topic_object = models.asTopic(topic_dictionary)

    # urlMatches = [e for e in topic_object.subscribers if e["deviceURL"] == deviceInfo.deviceURL]

    urlMatches = [a for a in topic_object.subscribers if models.asDeviceInfo(a).deviceURL == deviceInfo.deviceURL]

    # print(urlMatches[0])

    if urlMatches.__len__() > 1:
        print("Error: Registry issue")
        return 0, None
    elif urlMatches.__len__() == 1:
        print("Already subscribed")
        return 0, models.asDeviceInfo(urlMatches[0])
    else:
        print("Not subscribed, registering user now")

        # generate device id
        newID = topic_object.subscribers.__len__()

        # set device id
        deviceInfo.deviceID = newID

        # update object
        topic_object.subscribers.append(deviceInfo)

        # store device id to file
        dbHelper.json_to_file(dataObjAsDict=topic_object.asDict(), topicName=topic)

        return 1, deviceInfo

# registerSubscriber()
