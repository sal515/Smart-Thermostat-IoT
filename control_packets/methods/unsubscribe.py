import control_packets as cp

# 3.10 UNSUBSCRIBE - Unsubscribe from topics

class unsubscribe():

    @staticmethod
    def extract_payload_data(packet_info: cp.processing):
        # print(packet_info.reduced_bytes)
        while True:
            topic_qos_pair = []
            if packet_info.reduced_bytes.__len__() < 2:
                return
            topic_qos_pair.append(cp.extract_string(packet_info))
            packet_info.subscribed_topics.append(topic_qos_pair)
