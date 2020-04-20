import control_packets as cp


# 3.13 PINGRESP – PING response
class pingresp():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        pingresp.create_fixed_header(packet)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(208)
        packet.append(0)
