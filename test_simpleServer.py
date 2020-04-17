import socketserver
import socket


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.print_socket_details()

        clientAddress = self.client_address
        # self.

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        received_bytes: bytes = self.data
        received_bytes_list: [] = []
        remaining_received_bytes_list: [] = []

        for byte in received_bytes:
            received_bytes_list.append(byte)
            remaining_received_bytes_list.append(byte)

        packet_type = None
        remaining_length_bytes_arr = []
        remaining_length = -1

        index = -1
        for byte in received_bytes_list:

            remaining_received_bytes_list.pop(0)
            index += 1

            if index == 0:
                # Fixme : Flag bits needs to be taken care of
                # print(hex(byte))
                packet_type = byte >> 4

            elif index == 1:
                remaining_length_bytes_arr.append(byte)

            elif index == 2:
                remaining_length_bytes_arr.append(byte)

                "Remaining Length calculation"
                multiplier = 1
                remaining_length = 0

                # while True:
                for encodedByte in remaining_length_bytes_arr:
                    try:
                        # encodedByte = byte
                        remaining_length += (encodedByte & 127) * multiplier
                        multiplier *= 128

                        if multiplier > (128 * 128 * 128):
                            raise ValueError
                        if (encodedByte & 128) == 0:
                            break

                    except Exception as e:
                        print("Error calculating remaining length: {}".format(e))
                        break
                # print(remaining_length)

        self.process_packet(packet_type, remaining_length)

            # must be be incremented at the end of the loop
            # print(hex(byte))
            # print(index)

        # print(type(self.data))
        # received_data: bytes = self.data
        # # print(received_data.decode("utf-8"))
        # print(received_data.decode("ascii"))

        # # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

    def process_packet(self, packet_type, remaining_length):
        print("Packet type: ",  packet_type)
        print("Remaining length: ",  remaining_length)

        if packet_type == 0:
            print("Reserved")

        elif packet_type == 1:
            print("CONNECT")

        elif packet_type == 2:
            print("CONNACK")

        elif packet_type == 3:
            print("PUBLISH")

        elif packet_type == 4:
            print("PUBACK")

        elif packet_type == 5:
            print("PUBREC")

        elif packet_type == 6:
            print("PUBREL")

        elif packet_type == 7:
            print("PUBCOMP")

        elif packet_type == 8:
            print("SUBSCRIBE")

        elif packet_type == 9:
            print("SUBACK")

        elif packet_type == 10:
            print("UNSUBSCRIBE")

        elif packet_type == 11:
            print("UNSUBACK")

        elif packet_type == 12:
            print("PINGREQ")

        elif packet_type == 13:
            print("PINGRESP")

        elif packet_type == 14:
            print("DISCONNECT")

        else:
            print("forbidden")

    def print_socket_details(self):
        print(self.request)

        # sock: socket.socket = None
        sock: socket.socket = self.request
        sockFamily = sock.family
        sockType = sock.type
        sockProto = sock.proto
        sockLaddr = sock.getsockname()
        sockRaddr = sock.getpeername()
        sockFd = sock.fileno()
        print(sockFamily)
        print(sockType)
        print(sockProto)
        print(sockLaddr)
        print(sockRaddr)
        print(sockFd)


if __name__ == "__main__":
    myIP = socket.gethostbyname(socket.gethostname())
    HOST, PORT = myIP, 1883

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
