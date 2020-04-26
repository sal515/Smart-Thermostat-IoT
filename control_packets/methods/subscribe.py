import control_packets as cp
import databaseHelper.sql_helpers.db_helper as sqlHelper


# 3.8 SUBSCRIBE - Subscribe to topics
class subscribe():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)
        while True:
            topic_qos_pair = []
            if packet_info.reduced_bytes.__len__() < 2:
                return
            topic_qos_pair.append(cp.extract_string(packet_info))
            topic_qos_pair.append(packet_info.pop_a_msb())
            packet_info.subscribed_topics.append(topic_qos_pair)

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):

        iterations = 2
        for index in range(0, iterations):

            if packet_info.reduced_bytes.__len__() < iterations:
                raise Exception("Error in packet size, can not get variable packet header ")

            byte = packet_info.reduced_bytes[0]
            packet_info.pop_a_msb()

            # print("byte:", byte)

            if index == 0:
                if byte != 0:
                    raise Exception("Invalid packet identifier 1")
                packet_info.packet_identifier = ((byte & 255) << 8)
                packet_info.packet_identifier_msb = byte

            # FIXME : Paho request of subscribe doesnt' match documentation of MQTTv311 section 3.8.2.1, figure 3.21
            # Documentation says the packet identifier lsb should be 10
            # But the paho is sending the packet identifier lsb equal to 1

            elif index == 1:
                # if byte != 10:
                #     print(byte)
                #     raise Exception("Invalid packet identifier 2")
                packet_info.packet_identifier = packet_info.packet_identifier | (byte & 255)
                # packet_info.packet_identifier_lsb = 10
                packet_info.packet_identifier_lsb = byte

    @staticmethod
    def update_subscribers_database(packet_info: cp.processing):
        # Storing user address to the database
        source = packet_info.sock.getpeername()
        new_topics = []
        for topic in packet_info.subscribed_topics:

            # check if the user already exist
            client = sqlHelper.get_client_by_name_ip_one_or_none(session=packet_info.session,
                                                                 client_name=packet_info.thread_current_client_name,
                                                                 client_ip=source[0])

            # create a new user if doesn't exist
            if client is None:
                client = sqlHelper.create_client(client_name=packet_info.thread_current_client_name, client_ip=source[0],
                                                 client_port=source[1], client_qos=packet_info.qosLevel, client_type="sub")

            # FIXME: QOS is updated - Needs more handling?
            client.client_qos = packet_info.qosLevel
            client.client_port = source[1]

            if client.client_type is None:
                client.client_type = "sub"
            else:
                client.client_type = "pub/sub"

            # access existing topic
            topic_obj = sqlHelper.get_topic_one_or_none(packet_info.session, topic[0])

            # create a new topic - if doesn't exist
            if topic_obj is None:
                topic_obj = sqlHelper.create_topic(topic_name=topic[0], messages=[], clients=[client])
                new_topics.append(topic_obj)
                continue

            topic_obj.clients.append(client)
            # new_topics.append(topic_obj)
        # adding new topics
        packet_info.session.add_all(new_topics)
