import control_packets as cp


class info:
    invalid: bool = False
    _received_bytes = None
    _received_bytes_list: [] = []
    remaining_received_bytes: [] = []

    _remaining_length = []

    packet_type = None
    remaining_length = -1

    byte_arr_index = -1

    def __init__(self, received_bytes):
        self._received_bytes = received_bytes

        for byte in received_bytes:
            self._received_bytes_list.append(byte)
            self.remaining_received_bytes.append(byte)

        print(self.remaining_received_bytes)

        self.__identify_packet_type_size()

    def __identify_packet_type_size(self):

        # self.byte_arr_index = -1

        for byte in self._received_bytes_list:

            # increment the index of the byte being processed
            self.byte_arr_index += 1

            if self.byte_arr_index == 0:
                # Fixme : Flag bits needs to be taken care of
                # print(hex(byte))
                self.packet_type = byte >> 4

            elif self.byte_arr_index == 1:
                self._remaining_length.append(byte)

            elif self.byte_arr_index == 2:
                self._remaining_length.append(byte)
                self.__calculate_remaining_size()

            elif self.byte_arr_index == 3:
                if byte != 0:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            elif self.byte_arr_index == 4:
                if byte != 4:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            elif self.byte_arr_index == 5:
                if byte != 77:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            elif self.byte_arr_index == 6:
                if byte != 81:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            elif self.byte_arr_index == 7:
                if byte != 84:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            elif self.byte_arr_index == 8:
                if byte != 84:
                    self.invalid = True
                    raise Exception("Invalid Protocol")

            else:
                self.byte_arr_index -= 1
                return

            # pop out the byte that was just process in this iteration
            removed_byte = self.remaining_received_bytes.pop(0)

            # print(self.byte_arr_index)
            # print(removed_byte)

    def __calculate_remaining_size(self):
        # "Remaining Length calculation"
        multiplier = 1
        self.remaining_length = 0
        # while True:
        for encodedByte in self._remaining_length:
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

    def process_packet(self):
        # print("Packet type: ", self.packet_type)
        # print("Remaining length: ", self.remaining_length)

        if self.packet_type == 0:
            print("Reserved")

        elif self.packet_type == 1:
            print("CONNECT")

        elif self.packet_type == 2:
            print("CONNACK")

        elif self.packet_type == 3:
            print("PUBLISH")

        elif self.packet_type == 4:
            print("PUBACK")

        elif self.packet_type == 5:
            print("PUBREC")

        elif self.packet_type == 6:
            print("PUBREL")

        elif self.packet_type == 7:
            print("PUBCOMP")

        elif self.packet_type == 8:
            print("SUBSCRIBE")

        elif self.packet_type == 9:
            print("SUBACK")

        elif self.packet_type == 10:
            print("UNSUBSCRIBE")

        elif self.packet_type == 11:
            print("UNSUBACK")

        elif self.packet_type == 12:
            print("PINGREQ")

        elif self.packet_type == 13:
            print("PINGRESP")

        elif self.packet_type == 14:
            print("DISCONNECT")

        else:
            print("forbidden")
