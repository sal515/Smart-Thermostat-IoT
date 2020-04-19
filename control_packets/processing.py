import control_packets as cp

class processing:

    def __init__(self, received_bytes):
        self.response_message = None
        # packet data - all headers
        self.bytes = None
        self.reduced_bytes: [] = []

        # fixed header
        self.type = None
        self.flags = None
        # remaining length is the length of variable header bytes + payload bytes
        self.remaining_length = -1

        # variable header
        self.protocol_level = None
        self.connect_flags: cp.connect_flags = cp.connect_flags(2)
        self.keep_alive = None

        # payload
        self.client_identifier: str = None
        self.will_topic = None
        self.will_message = None
        self.user_name = None
        self.password = None

        self.bytes = received_bytes

        for byte in received_bytes:
            self.reduced_bytes.append(byte)

        # print(self.reduced_bytes)

        self.__identify_packet_type()
        self.__calculate_remaining_size()
        self.process_packet()

    def process_packet(self):

        # print("Packet type: ", self.packet_type)
        # print("Remaining length: ", self.remaining_length)

        if self.type == 0:
            print("Reserved")

        elif self.type == 1:
            print("CONNECT")
            cp.connect.extract_variable_header(self)
            cp.connect.extract_payload_data(self)
            self.response_message = cp.connack.build(self)
            # print("connack msg built: ", cp.connack.build(self))
            # print("connack msg built in bytes: ", bytes(cp.connack.build(self)))

        elif self.type == 2:
            print("CONNACK")

        elif self.type == 3:
            print("PUBLISH")

        elif self.type == 4:
            print("PUBACK")

        elif self.type == 5:
            print("PUBREC")

        elif self.type == 6:
            print("PUBREL")

        elif self.type == 7:
            print("PUBCOMP")

        elif self.type == 8:
            print("SUBSCRIBE")
            # cp.connect.extract_variable_header(self)
            # cp.connect.extract_payload_data(self)
            # self.response_message = cp.connack.build(self)

        elif self.type == 9:
            print("SUBACK")

        elif self.type == 10:
            print("UNSUBSCRIBE")

        elif self.type == 11:
            print("UNSUBACK")

        elif self.type == 12:
            print("PINGREQ")

        elif self.type == 13:
            print("PINGRESP")

        elif self.type == 14:
            print("DISCONNECT")

        else:
            print("forbidden")

    def pop_a_msb(self):
        return self.reduced_bytes.pop(0)

    def __identify_packet_type(self):

        self.type = (self.bytes[0] & 240) >> 4
        self.flags = self.bytes[0] & 15
        self.pop_a_msb()
        # print(self.pop_a_msb())

    def __calculate_remaining_size(self):
        # "Remaining Length calculation"
        multiplier = 1
        self.remaining_length = 0

        for index in range(0, 2):
            try:
                encoded_byte = self.reduced_bytes[0]
                self.pop_a_msb()
                # print(self.pop_a_msb())

                self.remaining_length += (encoded_byte & 127) * multiplier
                multiplier *= 128

                if multiplier > (128 * 128 * 128):
                    raise ValueError

                if (encoded_byte & 128) == 0:
                    break

            except ValueError as e:
                print("Error calculating remaining length: {}".format(e))
                exit(-1)
                break
