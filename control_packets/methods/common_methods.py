import control_packets as cp


def extract_string(packet_info: cp.processing):
    msb = packet_info.pop_a_msb()
    lsb = packet_info.pop_a_msb()
    string_length = (msb << 1) | lsb
    ascii_list = []
    for c in range(0, string_length):
        ascii_list.append(packet_info.pop_a_msb())

    return "".join(chr(i) for i in ascii_list)
