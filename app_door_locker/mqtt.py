import paho.mqtt.client as mqtt
import databaseHelper as dbHelper
import json

database_fileName = "door_locker_info"


def create_client(client_id: str, clean_session: bool = True, userdata: {} = None, protocol=mqtt.MQTTv311,
                  transport="tcp"):
    return mqtt.Client(client_id=client_id, clean_session=clean_session, userdata=userdata, protocol=protocol,
                       transport=transport)


def connect(client, host: str, port: int = 1883, keepalive: int = 60, bind_address: str = ""):
    client.connect(host=host, port=port, keepalive=keepalive, bind_address=bind_address)


def enable_on_message_callbacks(client):
    client.on_message = on_message


def enable_callbacks(client):
    # client.on_message = on_message
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe
    client.on_publish = on_publish

    # client.will_set("aTopic", "client will msg", 2, True)
    # client.username_pw_set("me", "yes")


def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
          + message.topic + "' with QoS " + str(message.qos))

    data = json.loads(message.payload)
    if data["app_info"] == "0":
        return

    if not dbHelper.isfile(database_fileName):
        # Create empty user list information file
        dbHelper.json_to_file([], database_fileName)

    users_list: [] = dbHelper.file_to_json(database_fileName)

    index = -1
    user_exist = False
    for user in users_list:
        index += 1
        if user["user_name"] == data["user_name"]:
            user_exist = True
            break

    if user_exist:
        users_list[index]["temperature"] = data["temperature"]
        users_list[index]["app_info"] = "0"
        if data["app_info"] == "-1":
            users_list.pop(index)
    else:
        data["app_info"] = "0"
        users_list.append(data)

    dbHelper.json_to_file(users_list, database_fileName)


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
