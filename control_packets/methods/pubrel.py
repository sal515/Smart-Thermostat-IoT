import control_packets as cp

# 3.6 PUBREL- Publish Released

class pubrel():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        pubrel.create_fixed_header(packet)
        pubrel.create_variable_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(98)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)

