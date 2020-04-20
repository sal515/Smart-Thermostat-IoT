import control_packets as cp


# 3.9 SUBACK – Subscribe acknowledgement
class suback():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        suback.create_fixed_header(packet)
        suback.create_variable_header(packet, packet_info)
        suback.create_payload_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(144)
        # FIXME: what is remaining length
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)

    @staticmethod
    def create_payload_header(packet: [], packet_info: cp.processing):
        success_with_qos_0 = 0
        success_with_qos_1 = 1
        success_with_qos_2 = 2
        failure = 128

        # FIXME : Logic to choose with QoS is not implemented

        # print("# of topics:", packet_info.topics.__len__())
        topics_num = packet_info.topics.__len__()
        for i in range(0, topics_num):
            packet.append(success_with_qos_0)
            packet[1] += 1

    @staticmethod
    def increment_remaining_length(packet: []):
        packet[1] += 1
