import control_packets as cp

# 3.6 PUBCOMP - Publish Complete

class pubcomp():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        pubcomp.create_fixed_header(packet)
        pubcomp.create_variable_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(112)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)

