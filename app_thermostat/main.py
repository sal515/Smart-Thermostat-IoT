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


# # Conversions between dict and object test
# tim = model.userInfo("Tim", 19, False)
# hancock = model.userInfo("Hancock", 24, True)
# plo = model.userInfo("Plo", 21, True)
#
# # print(tim.asDict()["name"])
# # print(model.asUserInfo(tim.asDict()))
# # print(tim)

# # Test to save userInfo object to file and read it back as object
# db.json_to_file(tim.asDict(), topicsJson, databaseDirectoryName)
# userdata = db.file_to_json(topicsJson, databaseDirectoryName)
# timA = model.asUserInfo(userdata)
# print(tim.name)

# # Testing mosquitto app_broker with  the python paho mqtt client library
# import paho.mqtt.client as mqtt
# import time
# import socket
#
# def on_message(client, userdata, message):
#     print("message received --> ", str(message.payload.decode("utf-8")))
#     print("message topic -->", message.topic)
#     print("message qos -->", message.qos)
#     print("message retain flag -->", message.retain)
#
#
# myIP = socket.gethostbyname(socket.gethostname())
# topic = "yes/no"
#
# client = mqtt.Client("thermostat")
# client.connect(myIP)
#
# # receiver = mqtt.Client("app")
# # receiver.on_message = on_message
# # receiver.connect(myIP)
#
# client.on_message = on_message
# client.connect(myIP)
# client.subscribe(topic)
#
# # client.publish(topic, "yes")
#
# client.loop_start()  # start the loop
# print("Subscribing to topic", topic)
# client.subscribe(topic)
# print("Publishing message to topic", topic)
# client.publish(topic, "off")
# time.sleep(4)  # wait
# client.loop_stop()  # stop the loop
