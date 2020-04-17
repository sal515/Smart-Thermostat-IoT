# 3.1 CONNECT – Client requests a connection to a Server
class connect():
    def get(self):
        pass


# 3.2 CONNACK – Acknowledge connection request
class connack():
    pass


# 3.3 PUBLISH – Publish message
class publish():
    pass


# 3.4 PUBACK – Publish acknowledgement
class puback():
    pass


# 3.5 PUBREC – Publish received (QoS 2 publish received, part 1)
class pubrec():
    pass


# 3.6 PUBREL – Publish release (QoS 2 publish received, part 2)
class pubrel():
    pass


# 3.7 PUBCOMP – Publish complete (QoS 2 publish received, part 3)
class pubcomp():
    pass


# 3.8 SUBSCRIBE - Subscribe to topics
class subscribe():
    pass


# 3.9 SUBACK – Subscribe acknowledgement
class suback():
    pass


# 3.10 UNSUBSCRIBE – Unsubscribe from topics
class unsubscribe():
    pass


# 3.11 UNSUBACK – Unsubscribe acknowledgement
class unsuback():
    pass


# 3.12 PINGREQ – PING request
class pingreq():
    pass


# 3.13 PINGRESP – PING response
class pingresp():
    pass


# 3.14 DISCONNECT – Disconnect notification
class disconnect():
    pass
