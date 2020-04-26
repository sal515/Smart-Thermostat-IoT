import control_packets as cp
import databaseHelper.sql_helpers.db_helper as sqlHelper


# 3.3 PUBLISH – Publish message
class publish():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)

        len = packet_info.reduced_bytes.__len__()

        while len != 0:
            len -= 1
            packet_info.published_message.append(packet_info.pop_a_msb())

    @staticmethod
    def extract_variable_header(packet_info: cp.processing):
        if packet_info.reduced_bytes.__len__() < 2:
            raise Exception("Topic name not found")

        packet_info.published_topic = cp.extract_string(packet_info)
        if (packet_info.qosLevel == 1) or (packet_info.qosLevel == 2):
            packet_info.packet_identifier_msb = packet_info.pop_a_msb()
            packet_info.packet_identifier_lsb = packet_info.pop_a_msb()

    @staticmethod
    def publish_to_subscribers(packet_info: cp.processing):

        # === Storing user address to the database ===
        source = packet_info.sock.getpeername()
        published_msg_str = cp.get_message_str(packet_info.published_message)
        message = sqlHelper.create_message(published_msg_str)

        # check if user already exists
        client = sqlHelper.get_client_by_name_ip_one_or_none(session=packet_info.session,client_name=packet_info.thread_current_client_name,client_ip=source[0])

        # create a new user if doesn't exist
        if client is None:
            client = sqlHelper.create_client(client_name=packet_info.thread_current_client_name, client_ip=source[0],
                                             client_port=source[1], client_qos=packet_info.qosLevel, client_type="pub")

        # FIXME: QOS is updated - Needs more handling?
        client.client_qos = packet_info.qosLevel
        client.client_port = source[1]

        if client.client_type is None:
            client.client_type = "pub"
        else:
            client.client_type = "pub/sub"

        # access existing topic
        topic_obj = sqlHelper.get_topic_one_or_none(packet_info.session, packet_info.published_topic)
        # create a new topic - if doesn't exist
        if topic_obj is None:
            topic_obj = sqlHelper.create_topic(topic_name=packet_info.published_topic, messages=[message],
                                               clients=[client])
            packet_info.session.add(topic_obj)

        else:
            topic_obj.messages.append(message)
            topic_obj.clients.append(client)
            packet_info.session.add(topic_obj)

        packet_info.session.commit()

        # === publishing message received to subscribed users ===
        clients = topic_obj.clients

        # subscribed_clients = []
        for client in clients:
            if client.client_type == "sub" or client.client_type == "pub/sub":
                packet_info.publish_to_clients_list.append(client)
                # subscribed_clients.append(client)

        print("publish_to_clients_list :: ", packet_info.publish_to_clients_list)



        # send_message = [48, 93, 0, 20, 115, 109, 97, 114, 116, 95, 104, 111, 109, 101, 47, 117, 115, 101, 114,
        #                 95, 100, 97, 116, 97, 123, 34, 97, 112, 112, 95, 105, 110, 102, 111, 34, 58, 32, 34, 49,
        #                 34, 44, 32, 34, 105, 115, 95, 104, 111, 109, 101, 34, 58, 32, 34, 48, 34, 44, 32, 34,
        #                 116, 101, 109, 112, 101, 114, 97, 116, 117, 114, 101, 34, 58, 32, 34, 50, 34, 44, 32,
        #                 34, 117, 115, 101, 114, 95, 110, 97, 109, 101, 34, 58, 32, 34, 115, 34, 125]
        #
        # packet_info.sock.sendall(bytes(send_message))