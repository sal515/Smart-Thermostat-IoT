import control_packets as cp



# 3.11 UNSUBACK – Unsubscribe acknowledgement
class unsuback():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        unsuback.create_fixed_header(packet)
        unsuback.create_variable_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(176)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)


