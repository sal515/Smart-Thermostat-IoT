import control_packets as cp


# 3.8 SUBSCRIBE - Subscribe to topics
class subscribe():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)
        while True:
            topic_qos_pair = []
            if packet_info.reduced_bytes.__len__() < 2:
                return
            topic_qos_pair.append(cp.extract_string(packet_info))
            topic_qos_pair.append(packet_info.pop_a_msb())
            packet_info.topics.append(topic_qos_pair)

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
