import paho.mqtt.client as mqtt
import databaseHelper as dbHelper
import json

current_temperature = 15


def create_client(client_id: str, clean_session: bool = True, userdata: {} = None, protocol=mqtt.MQTTv311,
                  transport="tcp"):
    return mqtt.Client(client_id=client_id, clean_session=clean_session, userdata=userdata, protocol=protocol,
                       transport=transport)


def connect(client, host: str, port: int = 1883, keepalive: int = 60, bind_address: str = ""):
    client.connect(host=host, port=port, keepalive=keepalive, bind_address=bind_address)


def enable_callbacks(client):
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe
    client.on_publish = on_publish

    # client.will_set("aTopic", "client will msg", 2, True)
    # client.username_pw_set("me", "yes")


def on_message(client, userdata, message):
    global current_temperature

    # print("Received message '" + str(message.payload) + "' on topic '"
    #       + message.topic + "' with QoS " + str(message.qos))

    data = json.loads(message.payload)
    if data["app_info"] == "-1":
        return

    # if not dbHelper.isfile("user_information"):
    #     # Create empty user list information file
    #     dbHelper.json_to_file([], "user_information")

    users_list: [] = dbHelper.file_to_json("user_information")
    active_list: [] = dbHelper.file_to_json("active_users")

    index = -1
    user_exist = False
    for user in users_list:
        index += 1
        if user["user_name"] == data["user_name"]:
            user_exist = True
            break

    if user_exist:
        if users_list[index]["is_home"] == "0" and data["is_home"] == "1":
            #     user entered the house
            active_list.append(data)

        elif users_list[index]["is_home"] == "1" and data["is_home"] == "0":
            #     user left the house
            i = -1
            for user in active_list:
                i += 1
                if user["user_name"] == data["user_name"]:
                    active_list.pop(i)
                    break
        users_list[index] = data

    else:
        users_list.append(data)
        if data["is_home"] == "1":
            active_list.append(data)

    dbHelper.json_to_file(users_list, "user_information")
    dbHelper.json_to_file(active_list, "active_users")

    # Set temperature

    # Empty house
    if active_list.__len__() < 1:
        # Temperature = 15
        current_temperature = 15
        print("Empty house, temperature set to: {}".format(current_temperature))

    # Active users
    else:
        # Temperature set to the first person entered - preference
        current_temperature = active_list[0]["temperature"]
        print("Temperature set to {}'s preference: {}".format(active_list[0]["user_name"], current_temperature))


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: {}".format(mqtt.connack_string(rc)))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed")
    pass


def on_unsubscribe(client, userdata, mid):
    print("Unsubscribed")
    pass


def on_publish(client, userdata, mid):
    print("Published : {}".format(mid))
    pass


def on_socket_open(client, userdata, sock):
    print("Connection opened and returned result: {}".format(mqtt.connack_string(sock)))
    pass


def on_socket_close(client, userdata, sock):
    print("Connection closed and returned result: {}".format(mqtt.connack_string(sock)))
    pass
