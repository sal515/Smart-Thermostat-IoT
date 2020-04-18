# Testing mosquitto broker with  the python paho mqtt client library
import paho.mqtt.client as mqtt
import time
import socket


def on_message(client, userdata, message):
    print("message received --> ", str(message.payload.decode("utf-8")))
    print("message topic -->", message.topic)
    print("message qos -->", message.qos)
    print("message retain flag -->", message.retain)


myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
topic = "yes/no"



client = mqtt.Client(client_id="tttttttttt", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")


client.will_set("aTopic", "client will msg", 2, True)
client.username_pw_set("me", "yes")

# client = mqtt.Client(client_id="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",    clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

# client.connect(host=myIP, port=1883, keepalive=60, bind_address="")
client.connect(host=myIP, port=1881, keepalive=9999, bind_address="")

client.on_message = on_message

client.loop_start()  # start the loop
# # print("Subscribing to topic", topic)
# client.subscribe(topic)
# # print("Publishing message to topic", topic)
# client.publish(topic, "off")
# time.sleep(4)  # wait
client.loop_stop()  # stop the loop
