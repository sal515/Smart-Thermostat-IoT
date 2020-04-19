# Testing mosquitto broker with  the python paho mqtt client library
import paho.mqtt.client as mqtt
import time
import socket


def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
          + message.topic + "' with QoS " + str(message.qos))


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: {}".format(mqtt.connack_string(rc)))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_subscribe(client, userdata, mid, granted_qos):
    # print("Connection returned result: {}".format(mqtt.connack_string(rc)))
    pass


def on_unsubscribe(client, userdata, mid):
    # print("Connection returned result: {}".format(mqtt.connack_string(rc)))
    pass


def on_publish(client, userdata, mid, granted_qos):
    # print("Connection returned result: {}".format(mqtt.connack_string(rc)))
    pass


def on_socket_open(client, userdata, sock):
    # print("Connection returned result: {}".format(mqtt.connack_string(rc)))
    pass


def on_socket_close(client, userdata, sock):
    # print("Connection returned result: {}".format(mqtt.connack_string(rc)))
    pass


myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
topic = "yes/no"

client = mqtt.Client(client_id="tttttttttt", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

# client = mqtt.Client(client_id="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",    clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
# client.will_set("aTopic", "client will msg", 2, True)
# client.username_pw_set("me", "yes")


# client.connect(host=myIP, port=1883, keepalive=10, bind_address="")
client.connect(host=myIP, port=1881, keepalive=10, bind_address="")

client.loop_start()  # start the loop

# # print("Subscribing to topic", topic)
# client.subscribe(topic)
# # print("Publishing message to topic", topic)
# client.publish(topic, "off")
time.sleep(10)  # wait
client.loop_stop()  # stop the loop
