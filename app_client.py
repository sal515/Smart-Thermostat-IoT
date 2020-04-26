# Assumption:
# User name is unique across all the client applicaiton


# Testing mosquitto broker with  the python paho mqtt client library
import time
import json
import socket
import app_client.mqtt as mqtt_functions
import app_client.ui as ui
import databaseHelper as dbHelper

database_fileName = "user_info"

# MQTT and Network Variables
myIP = socket.gethostbyname(socket.gethostname())
serverIP = myIP
serverPort = 1883
# serverPort = 1881  # test server port
publish_topic_1 = "smart_home/user_data"
publish_topic_2 = "smart_home/presence_data"
# subscribe_topic_1 = "smart_home/thermostat"

client = mqtt_functions.create_client(client_id="app_client")
# mqtt_functions.enable_callbacks(client)
mqtt_functions.enable_on_message_callbacks(client)
mqtt_functions.connect(client, serverIP, serverPort)

#  Starting MQTT Client Loop
client.loop_start()  # start the loop

# App initialization

# App Variables
info_on_file = True
choices = 3
message: {} = {}

# Initialization of the application
info_on_file, message = ui.initialization(info_on_file, message)

while True:

    if not info_on_file:
        print("Program setup.")
        print("")

        message = ui.collect_user_name(message)
        message = ui.collect_temperature_preference(message)
        message["app_info"] = "1"

        # print(message)

        dbHelper.json_to_file(message, database_fileName)
        info_on_file = True

        # Publish updated message to the server
        client.publish(publish_topic_1, json.dumps(message))

    choice = ui.user_choice()
    while not choice.isdigit() or (int(choice) > choices or int(choice) < 0):
        print("Invalid input, please try again")
        choice = ui.user_choice()

    if choice == "0":
        message = ui.collect_temperature_preference(message)
        dbHelper.json_to_file(message, database_fileName)

        # Publish updated message to the server
        client.publish(publish_topic_1, json.dumps(message))

    elif choice == "1":
        message["app_info"] = "-1"
        dbHelper.json_to_file(message, database_fileName)
        info_on_file = False
        # Publish empty message - which will remove the user from list
        client.publish(publish_topic_1, json.dumps(message))
        client.publish(publish_topic_2, json.dumps(message))

    elif choice == "2":
        ui.display_current_information(message)
