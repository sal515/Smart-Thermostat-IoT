# Testing mosquitto broker with  the python paho mqtt client library
import socket
import app_thermostat.mqtt as mqtt_functions
import databaseHelper as dbHelper

user_database_fileName = "thermostat_user_info"
active_user_database_fileName = "thermostat_active_user_info"


def initialization():
    if not dbHelper.isfile(user_database_fileName):
        # Create empty user list information file
        dbHelper.json_to_file([], user_database_fileName)

    if not dbHelper.isfile(active_user_database_fileName):
        # Create empty active user list information file
        dbHelper.json_to_file([], active_user_database_fileName)


# MQTT and Network Variables
myIP = socket.gethostbyname(socket.gethostname())
serverIP = myIP
serverPort = 1883
# serverPort = 1881  # test server port
# subscribe_topic_1 = "smart_home/thermostat"
subscribe_topic_1 = "smart_home/presence_data"

client = mqtt_functions.create_client(client_id="thermostat")
# mqtt_functions.enable_callbacks(client)
mqtt_functions.enable_on_message_callbacks(client)
mqtt_functions.connect(client, serverIP, serverPort)

#  Starting MQTT Client Loop
client.loop_start()  # start the loop

client.subscribe(subscribe_topic_1)

# App initialization

# Initialization of the application
initialization()

while True:
    pass
