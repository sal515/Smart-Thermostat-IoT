import control_packets as cp


# 3.3 PUBLISH – Publish message
class publish():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)

        len = packet_info.reduced_bytes.__len__()

        while len != 0:
            len -= 1
            packet_info.published_message.append(packet_info.pop_a_msb())

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):
        if packet_info.reduced_bytes.__len__() < 2:
            raise Exception("Topic name not found")

        packet_info.published_topic = cp.extract_string(packet_info)
        if (packet_info.qosLevel == 1) or (packet_info.qosLevel == 2):
            packet_info.packet_identifier_msb = packet_info.pop_a_msb()
            packet_info.packet_identifier_lsb = packet_info.pop_a_msb()
