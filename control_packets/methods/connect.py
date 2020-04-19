import control_packets as cp


# 3.1 CONNECT – Client requests a connection to a Server
class connect():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)

        if not packet_info.reduced_bytes.__len__() < 2:
            # Extract client id
            packet_info.client_identifier = connect.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.will_flag:
            # Extract will topic
            packet_info.will_topic = connect.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.will_flag:
            # Extract will message
            packet_info.will_message = connect.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.user_name:
            # Extract user name
            packet_info.user_name = connect.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.password:
            # Extract password
            packet_info.password = connect.extract_message(packet_info)

    @staticmethod
    def extract_message(packet_info: cp.processing):
        msb = packet_info.pop_a_msb()
        lsb = packet_info.pop_a_msb()
        string_length = (msb << 1) | lsb
        ascii_list = []
        for c in range(0, string_length):
            ascii_list.append(packet_info.pop_a_msb())

        return "".join(chr(i) for i in ascii_list)

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):

        iterations = 10
        for index in range(0, iterations):

            if packet_info.reduced_bytes.__len__() < iterations:
                raise Exception("Error in packet size, can not get variable packet header ")

            byte = packet_info.reduced_bytes[0]
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
                packet_info.protocol_level = byte

            elif index == 7:
                packet_info.connect_flags = cp.connect_flags(byte)

            elif index == 8:
                packet_info.keep_alive = (byte & 255) << 8

            elif index == 9:
                packet_info.keep_alive = packet_info.keep_alive | (byte & 255)
