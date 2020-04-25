# Assumption: Once client per device ip
# Assumption: Publisher can publish to one topic per call

import time

import control_packets as cp
import socket
import threading
import socketserver

import databaseHelper.sql_helpers.db_helper as sqlHelper

# Create engine at the beginning of the app
engine = sqlHelper.create_database()


# recover message
# msgStr = ''.join(chr(i) for i in message)
# msgStr = bytes(m).decode()

def get_message_str(msg):
    return bytes(msg).decode()


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    # class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):

    client_identifier = None

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
        print("sock_family: ", sock_family)
        print("sock_type: ", sock_type)
        print("sock_proto: ", sock_proto)
        print("sock_laddr_destination: ", sock_laddr)
        print("sock_raddr_source: ", sock_raddr)
        print("sock_fd: ", sock_fd)

    def handle(self):
        while 1:

            # database session
            # Create session when new data is required
            db_session = sqlHelper.create_session(engine)

            self.print_socket_details()

            # receiving packet
            # data = str(self.request.recv(1024), 'ascii')
            # data = (self.request.recv(1024), 'ascii')

            data = (self.request.recv(1024))

            print("received by server: ", data)

            if not data:
                break

            # processing received packets
            try:
                packet_info = cp.processing(data, self, db_session)

                if self.client_identifier is None:
                    self.client_identifier = packet_info.client_identifier

                print("client_identifier: ", self.client_identifier)

                db_session.commit()

                debug = 1
                # debug = 0
                if debug:
                    print(" ")
                    print("==== Processed new packet of type : {} ====".format(packet_info.type))

                    print("packet_type: ", packet_info.type)
                    print("dupFlag: ", packet_info.dupFlag)
                    print("qosLevel: ", packet_info.qosLevel)
                    print("retain: ", packet_info.retain)
                    print("packet_remaining_length: ", packet_info.remaining_length)

                    print("packet_protocol_level: ", packet_info.protocol_level)
                    print("packet_connect_flags: ", packet_info.connect_flags.asDict())
                    print("packet_keep_alive: ", packet_info.keep_alive)
                    print("packet_identifier: ", packet_info.packet_identifier)
                    print("packet_identifier msb: ", packet_info.packet_identifier_msb)
                    print("packet_identifier lsb: ", packet_info.packet_identifier_lsb)
                    print("packet_identifier: ", packet_info.packet_identifier)
                    print("published_topic: ", packet_info.published_topic)

                    print("packet_client_identifier: ", packet_info.client_identifier)
                    print("packet_will_topic: ", packet_info.will_topic)
                    print("packet_will_message: ", packet_info.will_message)
                    print("packet_user_name: ", packet_info.user_name)
                    print("packet_password: ", packet_info.password)
                    print("subscribed_topics: ", packet_info.subscribed_topics)
                    print("published_message: ", packet_info.published_message)

                    print("packet remaining bytes in list: ", packet_info.reduced_bytes)

                    print("send: ", packet_info.send)
                    print("disconnect: ", packet_info.disconnect)

                    print(" ")
                    print("==== End of details for packet type:  {} ====".format(packet_info.type))
                    print(" ")

                #  sending response
                cur_thread = threading.current_thread()
                print("Current thread: ", cur_thread)

                if packet_info.send:
                    # response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
                    # response = bytes(packet_info.response_message)
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

        bytesArr = []
        for b in message:
            bytesArr.append(b)
        sock.sendall(bytes(bytesArr))
        response = (sock.recv(1024))
        # print("Received: {}".format(response))


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

        # debug = 0
        debug = 1
        if debug:
            # Test door monitor - subscribe
            # b'\x10\x1c\x00\x04MQTT\x04\x02\x00<\x00\x10door_lock_client'
            # b' \x02\x00\x00'
            # b'\x82\x19\x00\x01\x00\x14smart_home/user_data\x00'
            # b'\x90\x03\x00\x01\x00'

            # time.sleep(2)
            # client(HOST, PORT, b'\x10\x1c\x00\x04MQTT\x04\x02\x00<\x00\x10door_lock_client')
            # client(HOST, PORT, b'\x82\x19\x00\x01\x00\x14smart_home/user_data\x00')
            # time.sleep(2)
            # client(HOST, PORT, b' \x02\x00\x00')
            # time.sleep(2)
            # time.sleep(2)
            # client(HOST, PORT, b'\x90\x03\x00\x01\x00')

            #  ==== Random tests below ====

            # Test Connect
            # client(HOST, PORT, b'\x10\x1c\x00\x04MQTT\x04\x02\x00<\x00\x10door_lock_client')

            # Test subscribe
            # client(HOST, PORT, b'\x82\x17\x00\x01\x00\x03yes\x00\x00\x04yess\x00\x00\x05yesss\x00')

            # Test suback
            # client(ip, port, b'\x90\x05\x00\x01\x00\x00\x00')

            # Test publish
            # client(ip, port, b'0\x08\x00\x03yesoff')

            # Test pinreq
            # client(ip, port, b'\xc0\x00')

            # Test pinreqs
            # client(ip, port, b'\xd0\x00')
            pass

        server_thread.join()

        # while True:
        #     pass

        # server.shutdown()
