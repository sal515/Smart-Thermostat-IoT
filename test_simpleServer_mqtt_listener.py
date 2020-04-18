import socketserver
import socket
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.print_socket_details()

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        # print(self.data)

        # send received data from paho to mosquitto broker
        mosquitto_host = socket.gethostbyname(socket.gethostname())
        mosquitto_port = 1883
        send_data = self.data
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((mosquitto_host, mosquitto_port))

            print("Request to Mosquitto")
            print(send_data)
            sock.sendall(send_data)

            received_from_mosquitto_server = sock.recv(1024)
            print("Mosquitto's Response")
            print(received_from_mosquitto_server)

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
    HOST, PORT = myIP, 1881

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
