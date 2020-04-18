class info:
    invalid: bool = False
    received_bytes = None
    variable_payload_header: [] = []

    _remaining_length_bytes = []

    packet_type = None
    # remaining length is the length of variable header bytes + payload bytes
    remaining_length = -1

    def __init__(self, received_bytes):
        self.received_bytes = received_bytes

        for byte in received_bytes:
            self.variable_payload_header.append(byte)

        print(self.variable_payload_header)

        self.__identify_packet_type_size()

    def __identify_packet_type_size(self):

        index = -1

        for byte in self.received_bytes:

            # increment the index of the byte being processed
            index += 1

            if index == 0:
                # Fixme : Flag bits needs to be taken care of
                # print(hex(byte))
                self.packet_type = byte >> 4

            elif index == 1:
                self._remaining_length_bytes.append(byte)

            elif index == 2:
                self._remaining_length_bytes.append(byte)
                self.__calculate_remaining_size()

            else:
                # decrement the index to revert it to the last accessed position of the byte array
                index -= 1
                return

            # pop out the byte that was just process in this iteration
            removed_byte = self.pop_a_msb()
            # print(removed_byte)

    def pop_a_msb(self):
        return self.variable_payload_header.pop(0)

    def __calculate_remaining_size(self):
        # "Remaining Length calculation"
        multiplier = 1
        self.remaining_length = 0

        for encodedByte in self._remaining_length_bytes:
            try:
                # encodedByte = byte
                self.remaining_length += (encodedByte & 127) * multiplier
                multiplier *= 128

                if multiplier > (128 * 128 * 128):
                    raise ValueError
                if (encodedByte & 128) == 0:
                    break

            except Exception as e:
                print("Error calculating remaining length: {}".format(e))
                break
