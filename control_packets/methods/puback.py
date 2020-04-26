import control_packets as cp


# 3.4 PUBACK - Publish acknowledgement

class puback():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        puback.create_fixed_header(packet)
        puback.create_variable_header(packet, packet_info)
        return packet


    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(64)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)

