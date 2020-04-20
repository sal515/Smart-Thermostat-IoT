import socketserver
import socket

import control_packets as cp


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.print_socket_details()
        # clientAddress = self.client_address

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        # # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

        try:
            packet_info = cp.processing(self.data)

            print("packet_type: ", packet_info.type)
            print("packet_remaining_length: ", packet_info.remaining_length)
            print("packet_protocol_level: ", packet_info.protocol_level)
            print("packet_connect_flags: ", packet_info.connect_flags.asDict())
            print("packet_keep_alive: ", packet_info.keep_alive)

            print("packet_client_identifier: ", packet_info.client_identifier)
            print("packet_will_topic: ", packet_info.will_topic)
            print("packet_will_message: ", packet_info.will_message)
            print("packet_user_name: ", packet_info.user_name)
            print("packet_password: ", packet_info.password)

            print("packet remaining bytes in list: ", packet_info.reduced_bytes)

        except Exception as e:
            if e == "Invalid Protocol":
                print("Error: {}".format(e))
                exit(-1)
            else:
                print(e)
                exit(-2)

    def print_socket_details(self):
        print(self.request)

        # sock: socket.socket = None
        sock: socket.socket = self.request
        sock_family = sock.family
        sock_type = sock.type
        sock_proto = sock.proto
        sock_laddr = sock.getsockname()
        sock_raddr = sock.getpeername()
        sock_fd = sock.fileno()
        print(sock_family)
        print(sock_type)
        print(sock_proto)
        print(sock_laddr)
        print(sock_raddr)
        print(sock_fd)


if __name__ == "__main__":
    myIP = socket.gethostbyname(socket.gethostname())
    HOST, PORT = myIP, 1881

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print("Server running... ")
        server.serve_forever()
