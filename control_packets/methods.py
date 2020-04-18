import control_packets as cp


# 3.1 CONNECT – Client requests a connection to a Server
class connect():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_packet_bytes)

        if not packet_info.reduced_packet_bytes.__len__() < 2:
            # Extract client id
            packet_info.packet_client_identifier = connect.extract_message(packet_info)

        if (not packet_info.reduced_packet_bytes.__len__() < 2) and packet_info.packet_connect_flags.will_flag:
            # Extract will topic
            packet_info.packet_will_topic = connect.extract_message(packet_info)

        if (not packet_info.reduced_packet_bytes.__len__() < 2) and packet_info.packet_connect_flags.will_flag:
            # Extract will message
            packet_info.packet_will_message = connect.extract_message(packet_info)

        if (not packet_info.reduced_packet_bytes.__len__() < 2) and packet_info.packet_connect_flags.user_name:
            # Extract user name
            packet_info.packet_user_name = connect.extract_message(packet_info)

        if (not packet_info.reduced_packet_bytes.__len__() < 2) and packet_info.packet_connect_flags.password:
            # Extract password
            packet_info.packet_password = connect.extract_message(packet_info)

    @staticmethod
    def extract_message(packet_info):
        msb = packet_info.pop_a_msb()
        lsb = packet_info.pop_a_msb()
        string_length = (msb << 1) | lsb
        ascii_list = []
        for c in range(0, string_length):
            ascii_list.append(packet_info.pop_a_msb())

        return "".join(chr(i) for i in ascii_list)

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):

        for index in range(0, 10):

            if packet_info.reduced_packet_bytes.__len__() < 10:
                raise Exception("Error in packet size, can not get variable packet header ")

            byte = packet_info.reduced_packet_bytes[0]
            packet_info.pop_a_msb()

            # print("byte:", byte)

            if index == 0:
                if byte != 0:
                    raise Exception("Invalid Protocol (a)")

            elif index == 1:
                if byte != 4:
                    raise Exception("Invalid Protocol2 (b)")

            elif index == 2:
                if byte != 77:
                    raise Exception("Invalid Protocol (c)")

            elif index == 3:
                if byte != 81:
                    raise Exception("Invalid Protocol (d)")

            elif index == 4:
                if byte != 84:
                    raise Exception("Invalid Protocol (e)")

            elif index == 5:
                if byte != 84:
                    raise Exception("Invalid Protocol (f)")

            elif index == 6:
                packet_info.packet_protocol_level = byte

            elif index == 7:
                packet_info.packet_connect_flags = cp.connect_flags(byte)

            elif index == 8:
                packet_info.packet_keep_alive = (byte & 255) << 8

            elif index == 9:
                packet_info.packet_keep_alive = packet_info.packet_keep_alive | (byte & 255)


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
