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
        # self.print_socket_details()

        clientAddress = self.client_address
        # self.

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        print(type(self.data))
        received_data: bytes = self.data
        # print(received_data.decode("utf-8"))
        print(received_data.decode("ascii"))


        # # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

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
