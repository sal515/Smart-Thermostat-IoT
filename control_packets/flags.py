class connect_flags():
    def __init__(self, packet_connect_flags):
        self.reserved = 0
        self.clean_session = 0
        self.will_flag = 0
        self.will_qos = 0
        self.will_retain = 0
        self.password = 0
        self.user_name = 0

        self._will_qos_lsb = 0
        self._will_qos_msb = 0

        for counter in range(0, 8):
            bit = 1 << counter

            if packet_connect_flags & bit == 1:
                self.reserved = 1
                raise Exception("Reserved flag is set to 1. Exiting")

            elif packet_connect_flags & bit == 2:
                self.clean_session = 1

            elif packet_connect_flags & bit == 4:
                self.will_flag = 1

            elif packet_connect_flags & bit == 8:
                self._will_qos_lsb = 1

            elif packet_connect_flags & bit == 16:
                self._will_qos_msb = 1

            elif packet_connect_flags & bit == 32:

                self.will_retain = 1

            elif packet_connect_flags & bit == 64:
                self.password = 1

            elif packet_connect_flags & bit == 128:
                self.user_name = 1

            self.will_qos = (self._will_qos_msb << 1) | self._will_qos_lsb

            if self.will_qos > 2:
                raise Exception("will qos flag is wrong cannot be greater than 2")

    def asDict(self):
        return dict(reserved=self.reserved,
                    clean_session=self.clean_session,
                    will_flag=self.will_flag,
                    will_qos=self.will_qos,
                    will_retain=self.will_retain,
                    password=self.password,
                    user_name=self.user_name,
                    _will_qos_lsb=self._will_qos_lsb,
                    _will_qos_msb=self._will_qos_msb)

# class control_flags():
#     def __init__(self, packet_connect_flags):
#         self.reserved = 0
#         self.clean_session = 0
#         self.will_flag = 0
#         self.will_qos = 0
#         self.will_retain = 0
#         self.password = 0
#         self.user_name = 0
#
#         self._will_qos_lsb = 0
#         self._will_qos_msb = 0
#
#         for counter in range(0, 8):
#             bit = 1 << counter
#
#             if packet_connect_flags & bit == 1:
#                 self.reserved = 1
#                 raise Exception("Reserved flag is set to 1. Exiting")
#
#             elif packet_connect_flags & bit == 2:
#                 self.clean_session = 1
#
#             elif packet_connect_flags & bit == 4:
#                 self.will_flag = 1
#
#             elif packet_connect_flags & bit == 8:
#                 self._will_qos_lsb = 1
#
#             elif packet_connect_flags & bit == 16:
#                 self._will_qos_msb = 1
#
#             elif packet_connect_flags & bit == 32:
#
#                 self.will_retain = 1
#
#             elif packet_connect_flags & bit == 64:
#                 self.password = 1
#
#             elif packet_connect_flags & bit == 128:
#                 self.user_name = 1
#
#             self.will_qos = (self._will_qos_msb << 1) | self._will_qos_lsb
#
#             if (self.will_qos > 2):
#                 raise Exception("will qos flag is wrong cannot be greater than 2")
