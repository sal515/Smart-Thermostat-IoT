# Testing mosquitto broker with  the python paho mqtt client library
import socket
import app_door_locker.mqtt as mqtt_functions
import app_door_locker.ui as ui
import databaseHelper as dbHelper

# MQTT and Network Variables
myIP = socket.gethostbyname(socket.gethostname())
serverIP = myIP
serverPort = 1883
# serverPort = 1881  # test server port
topic_name = "smart_home/thermostat"

client = mqtt_functions.create_client(client_id="door_lock_client")
mqtt_functions.enable_callbacks(client)
mqtt_functions.connect(client, serverIP, serverPort)

#  Starting MQTT Client Loop
client.loop_start()  # start the loop

client.subscribe(topic_name)

# App initialization

# App Variables
choices = 2

# Initialization of the application
ui.initialization()

while True:

    choice = ui.user_choice()
    while not choice.isdigit() or (int(choice) > choices or int(choice) < 0):
        print("Invalid input, please try again")
        choice = ui.user_choice()

    if choice == "0":
        users_list: [] = dbHelper.file_to_json("user_information")

        index = ui.prompt_with_user_list(users_list)

        if users_list[index]["is_home"] == 1:
            users_list[index]["is_home"] = 0
        else:
            users_list[index]["is_home"] = 1

        dbHelper.json_to_file(users_list, "user_information")

        # Publish updated message to the server
        # client.publish(topic_name, json.dumps(users_list))

    elif choice == "1":
        users_list: [] = dbHelper.file_to_json("user_information")
        if users_list.__len__() < 1:
            print("")
            print("No users found to be able to modify presence.")
            print("")
            break

        index = -1
        print("List of users present in the house")
        for user in users_list:
            index += 1
            print("{} : UserName = {}, User_inside = {}".format(index, user["user_name"], user["is_home"]))

#  Test code below

# ==========================================
#
# client.loop_start()  # start the loop
#
# time.sleep(2)  # wait
#
# test_data = {
#     "is_home": "no",
#     "temperature": "11",
#     "user_name": "Salman"
# }
#
# test_data_s = json.dumps(test_data)
#
# # print("Subscribing to topic", topic_name)
# client.subscribe(topic_name)
# # print("Publishing message to topic", topic_name)
# client.publish(topic_name, test_data_s)
#
# time.sleep(2)  # wait
#
# # client.disconnect()
# #
# # time.sleep(15)  # wait
#
# client.loop_stop()  # stop the loop
