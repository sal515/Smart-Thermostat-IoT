import time

import control_packets as cp
import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
# class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):

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

    def handle(self):
        while 1:
            # receiving packet
            # data = str(self.request.recv(1024), 'ascii')
            # data = (self.request.recv(1024), 'ascii')

            data = (self.request.recv(1024))
            # data = (self.rfile.readline())
            print(data)

            if not data:
                break



            # processing received packets
            try:
                packet_info = cp.processing(data)

                debug = 0
                if debug:
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

                #  sending response
                cur_thread = threading.current_thread()
                # response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
                response = bytes(packet_info.response_message)
                print("response from server: ", response)
                self.request.sendall(response)

                # time.sleep(5)


            except Exception as e:
                if e == "Invalid Protocol":
                    print("Error: {}".format(e))
                    exit(-1)
                else:
                    print(e)
                    exit(-2)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    myIP = socket.gethostbyname(socket.gethostname())

    HOST, PORT = myIP, 1881

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        server_thread.join()

        # while True:
        #     pass

        # client(ip, port, "Hello World 1")
        # client(ip, port, "Hello World 2")
        # client(ip, port, "Hello World 3")

        # server.shutdown()
