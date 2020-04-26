import control_packets as cp

# 3.5 PUBREC- Publish Received

class pubrec():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        pubrec.create_fixed_header(packet)
        pubrec.create_variable_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(80)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        packet.append(packet_info.packet_identifier_msb)
        packet.append(packet_info.packet_identifier_lsb)

