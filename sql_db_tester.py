import databaseHelper.sql_helpers.db_helper as sqlHelper

import models as models

# Create engine at the beginning of the app
engine = sqlHelper.create_database()

# Create session when new data is required
session = sqlHelper.create_session(engine)

client1 = sqlHelper.create_client("111.111", 110, 1, "dev1", "pub")
client2 = sqlHelper.create_client(client_ip="222.222", client_port=220, client_qos=0, client_type="sub")

message1 = sqlHelper.create_message(name="Bel", temp=24.5, is_home=0)
message2 = sqlHelper.create_message(name="Al", temp=21.3, is_home=1)

topic1 = sqlHelper.create_topic(topic_name="Topic1", messages=[message1, message2], clients=[client1, client2])
topic2 = sqlHelper.create_topic(topic_name="Topic2", messages=[message1, message2], clients=[client1, client2])
topic3 = sqlHelper.create_topic(topic_name="Topic3", messages=[message1, message2], clients=[client1, client2])

# session.add(topic1)
# session.add(topic2)
# session.add(topic3)
session.add_all([topic1, topic2, topic3])

session.commit()

# session = sqlHelper.create_session(engine)
getTopic = sqlHelper.get_topic_by_name_first(session=session, topic_name="Topic1")
# session.commit()

printt = 0
# printt = 1
if printt:
    print("Topic ---> ", getTopic)
    print("Messages ---> ", getTopic.messages)
    print("Message 0 ---> ", getTopic.messages[0])
    print("Clients ---> ", getTopic.clients)
    print("Client 0 ---> ", getTopic.clients[0])
