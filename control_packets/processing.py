import control_packets as cp

class processing:

    def __init__(self, received_bytes):
        # packet data - all headers
        self.response_message = None
        self.send = False
        self.disconnect = False

        self.bytes = None
        self.reduced_bytes: [] = []

        # Variables

        # fixed header
        self.type = None
        self.dupFlag = None
        self.qosLevel = None
        self.retain = None
        self.remaining_length = -1

        # variable header
        self.protocol_level = None
        self.connect_flags: cp.connect_flags = cp.connect_flags(2)
        self.keep_alive = None
        self.packet_identifier_msb = None
        self.packet_identifier_lsb = None
        self.packet_identifier = None
        self.published_topic = None

        # payload
        self.client_identifier: str = None
        self.will_topic = None
        self.will_message = None
        self.user_name = None
        self.password = None
        self.subscribed_topics = []
        self.published_message = []

        # logic

        self.bytes = received_bytes

        for byte in received_bytes:
            self.reduced_bytes.append(byte)

        print(self.reduced_bytes)

        self.__identify_packet_type_n_flags()
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
            self.send = True
            # print("connack msg built: ", cp.connack.build(self))

        elif self.type == 2:
            print("CONNACK")
            # implemented
            pass

        elif self.type == 3:
            print("PUBLISH")
            cp.publish.extract_variable_header(self)
            cp.publish.extract_payload_data(self)

            self.send = False

            if self.qosLevel == 1:
                self.response_message = cp.puback.build(self)
                self.send = True

            elif self.qosLevel == 2:
                # Different implementation required
                self.response_message = cp.puback.build(self)
                self.send = True


        elif self.type == 4:
            print("PUBACK")
            # implemented
            pass

        elif self.type == 5:
            print("PUBREC")

        elif self.type == 6:
            print("PUBREL")

        elif self.type == 7:
            print("PUBCOMP")

        elif self.type == 8:
            print("SUBSCRIBE")
            cp.subscribe.extract_variable_header(self)
            cp.subscribe.extract_payload_data(self)
            self.response_message = cp.suback.build(self)
            self.send = True
            # print("suback msg: ", cp.suback.build(self))

        elif self.type == 9:
            print("SUBACK")
            # implemented
            pass

        elif self.type == 10:
            print("UNSUBSCRIBE")
            pass

        elif self.type == 11:
            print("UNSUBACK")
            pass

        elif self.type == 12:
            print("PINGREQ")
            self.response_message = cp.pingresp.build(self)
            self.send = True
            pass

        elif self.type == 13:
            print("PINGRESP")
            # implemented
            pass

        elif self.type == 14:
            print("DISCONNECT")
            self.disconnect = True
            pass

        else:
            print("forbidden")

    def pop_a_msb(self):
        return self.reduced_bytes.pop(0)

    def __identify_packet_type_n_flags(self):

        self.type = (self.bytes[0] & 240) >> 4
        self.__extract_all_flags_from_fixed_header(self.bytes[0] & 15)
        self.pop_a_msb()

    def __extract_all_flags_from_fixed_header(self, flags):
        self.dupFlag = flags >> 3

        if (flags & 4) >> 2 == 0 and (flags & 2) >> 1 == 0:
            self.qosLevel = 0
        if (flags & 4) >> 2 == 0 and (flags & 2) >> 1 == 1:
            self.qosLevel = 1
        if (flags & 4) >> 2 == 1 and (flags & 2) >> 0 == 1:
            self.qosLevel = 2

        self.retain = flags & 1

    def __calculate_remaining_size(self):
        # "Remaining Length calculation"
        multiplier = 1
        self.remaining_length = 0

        for index in range(0, 2):
            try:
                encoded_byte = self.reduced_bytes[0]
                self.pop_a_msb()

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
