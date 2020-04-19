import control_packets as cp


# 3.2 CONNACK – Acknowledge connection request
class connack():

    @staticmethod
    def build(packet_info: cp.processing):
        packet = []
        connack.create_fixed_header(packet)
        connack.create_variable_header(packet, packet_info)
        return packet

    @staticmethod
    def create_fixed_header(packet: []):
        packet.append(32)
        packet.append(2)

    @staticmethod
    def create_variable_header(packet: [], packet_info: cp.processing):
        _clean_session = packet_info.connect_flags.clean_session
        _identifier = packet_info.client_identifier

        _session_state = 0

        # FIXME : cp.is_session_stored -> Not Implemented in todo
        if not _clean_session and not cp.is_session_stored(_identifier):
            _session_state = 0

        if not _clean_session and cp.is_session_stored(_identifier):
            _session_state = 1

        # FIXME : determine_return_code not defined in todo
        packet.append(cp.determine_return_code())
        packet.append(_session_state)
