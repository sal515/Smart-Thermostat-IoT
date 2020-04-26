import control_packets as cp
import databaseHelper.sql_helpers.db_helper as sqlHelper

# 3.10 UNSUBSCRIBE - Unsubscribe from topics

class unsubscribe():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)
        while True:
            topics = []
            if packet_info.reduced_bytes.__len__() < 2:
                return
            topics.append(cp.extract_string(packet_info))
            packet_info.unsubscribed_topics.append(topics)

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):

        iterations = 2
        for index in range(0, iterations):

            if packet_info.reduced_bytes.__len__() < iterations:
                raise Exception("Error in packet size, can not get variable packet header ")

            byte = packet_info.reduced_bytes[0]
            packet_info.pop_a_msb()

            if index == 0:
                if byte != 0:
                    raise Exception("Invalid packet identifier 1")
                packet_info.packet_identifier = ((byte & 255) << 8)
                packet_info.packet_identifier_msb = byte

            elif index == 1:
                packet_info.packet_identifier = packet_info.packet_identifier | (byte & 255)
                packet_info.packet_identifier_lsb = byte

    @staticmethod
    def update_subscribers_database(packet_info: cp.processing):
        source = packet_info.sock.getpeername()

        for topic in packet_info.unsubscribed_topics:
            topic_obj = sqlHelper.get_topic_one_or_none(packet_info.session, topic[0])
            clients_list = topic_obj.clients

            for client in clients_list:
                if client.client_name == packet_info.thread_current_client_name:
                    packet_info.session.delete(client)








