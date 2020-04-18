import control_packets as cp


class processing:
    packet_bytes = None
    reduced_packet_bytes: [] = []

    packet_type = None
    packet_flags = None
    # remaining length is the length of variable header bytes + payload bytes
    packet_remaining_length = -1

    def __init__(self, received_bytes):
        self.packet_bytes = received_bytes

        for byte in received_bytes:
            self.reduced_packet_bytes.append(byte)

        print(self.reduced_packet_bytes)

        self.__identify_packet_type()
        self.__calculate_remaining_size()
        self.process_packet()

    def process_packet(self):

        # print("Packet type: ", self.packet_type)
        # print("Remaining length: ", self.remaining_length)

        if self.packet_type == 0:
            print("Reserved")

        elif self.packet_type == 1:
            print("CONNECT")
            cp.connect.extract_variable_header(self)

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

    def pop_a_msb(self):
        return self.reduced_packet_bytes.pop(0)

    def __identify_packet_type(self):

        self.packet_type = (self.packet_bytes[0] & 240) >> 4
        self.packet_flags = self.packet_bytes[0] & 15
        self.pop_a_msb()
        # print(self.pop_a_msb())



    def __calculate_remaining_size(self):
        # "Remaining Length calculation"
        multiplier = 1
        self.packet_remaining_length = 0

        for index in range(0, 2):
            try:
                encoded_byte = self.reduced_packet_bytes[0]
                removed_byte = self.pop_a_msb()
                # print(self.pop_a_msb())

                self.packet_remaining_length += (encoded_byte & 127) * multiplier
                multiplier *= 128

                if multiplier > (128 * 128 * 128):
                    raise ValueError

                if (encoded_byte & 128) == 0:
                    break

            except ValueError as e:
                print("Error calculating remaining length: {}".format(e))
                break
