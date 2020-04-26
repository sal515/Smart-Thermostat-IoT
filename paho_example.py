# Testing mosquitto broker with  the python paho mqtt client library
import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub
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
    print("Subscribed")
    pass


def on_unsubscribe(client, userdata, mid):
    # print("Unsubscribed")
    pass


def on_publish(client, userdata, mid):
    # print("Published : {}".format(mqtt. connack_string(rc)))
    print("Published : {}".format(mid))

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
topic = "yes"
topic1 = ("yes", 0)
topic2 = ("yess", 0)
topic3 = ("yesss", 0)

client = mqtt.Client(client_id="tttttttttt", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

# client = mqtt.Client(client_id="tttttttttt", clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")

# client = mqtt.Client(client_id="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",    clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_publish = on_publish

client.will_set("aTopic", "client will msg", 2, True)
# client.username_pw_set("me", "yes")


# client.connect(host=myIP, port=1883, keepalive=10, bind_address="")
client.connect(host=myIP, port=1881, keepalive=10, bind_address="")

client.loop_start()  # start the loop

time.sleep(2)  # wait

# # print("Subscribing to topic", topic)
# client.subscribe([topic1, topic2, topic3])
# # print("Publishing message to topic", topic)
# client.publish(topic, "off", 2, False)

client.publish(topic, "off", 2, False)

# msg = [{"topic": "t1", "payload": "Msg1", "qos": 0, "retain": False}, {"topic": "t2", "payload": "Msg2", "qos": 0, "retain": False}]
#
# pub.multiple(msg)

time.sleep(2)  # wait

# client.disconnect()
#
# time.sleep(15)  # wait


client.loop_stop()  # stop the loop
