import control_packets as cp


# 3.8 SUBSCRIBE - Subscribe to topics
class subscribe():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)

        if not packet_info.reduced_bytes.__len__() < 2:
            # Extract client id
            packet_info.client_identifier = subscribe.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.will_flag:
            # Extract will topic
            packet_info.will_topic = subscribe.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.will_flag:
            # Extract will message
            packet_info.will_message = subscribe.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.user_name:
            # Extract user name
            packet_info.user_name = subscribe.extract_message(packet_info)

        if (not packet_info.reduced_bytes.__len__() < 2) and packet_info.connect_flags.password:
            # Extract password
            packet_info.password = subscribe.extract_message(packet_info)

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

        iterations = 2
        for index in range(0, iterations):

            if packet_info.reduced_bytes.__len__() < iterations:
                raise Exception("Error in packet size, can not get variable packet header ")

            byte = packet_info.reduced_bytes[0]
            packet_info.pop_a_msb()

            # print("byte:", byte)

            if index == 0:
                if byte != 0:
                    raise Exception("Invalid packet identifier 1")
                packet_info.packet_identifier = ((byte & 255) << 8)

            # FIXME : Paho request of subscribe doesnt' match documentation of MQTTv311 section 3.8.2.1, figure 3.21
            # Documentation says the packet identifier lsb should be 10
            # But the paho is sending the packet identifier lsb equal to 1

            elif index == 1:
                # if byte != 10:
                #     print(byte)
                #     raise Exception("Invalid packet identifier 2")
                packet_info.packet_identifier = packet_info.packet_identifier | (byte & 255)
