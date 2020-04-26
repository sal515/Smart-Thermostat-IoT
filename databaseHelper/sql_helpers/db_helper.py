from sqlalchemy.orm import sessionmaker
import models as models
from sqlalchemy import create_engine

import databaseHelper.json_helpers.directory_helper as dir

dirName = "storage"
sql_db_name = 'sqlite:///{}//server.db'.format(dirName)


def create_database():
    dir.createDir(dirName)
    # Create tables if doesn't exist using base and engine
    engine = create_engine(sql_db_name, echo=False)
    models.Base.metadata.create_all(engine)
    return engine


def create_session(engine):
    # Store objects to db using sessions
    Session = sessionmaker(bind=engine)
    return Session()


def create_client(client_ip: str, client_port: int, client_qos: int, client_name: str = None, client_type: str = None):
    return models.client(client_name=client_name, client_ip=client_ip, client_port=client_port, client_qos=client_qos, client_type=client_type)


def create_message(message: str):
    return models.message(message=message)


def create_topic(topic_name: str, messages: [], clients: []):
    return models.topic(topic_name=topic_name, messages=messages, clients=clients)


def get_topic_by_name_first(session, topic_name: str):
    return session.query(models.topic).filter_by(topic_name=topic_name).first()


def get_client_by_name_ip_one_or_none(session, client_name: str, client_ip: str):
    return session.query(models.client).filter(models.client.client_name == client_name).filter(
        models.client.client_ip == client_ip).one_or_none()


def get_topic_one_or_none(session, topic_name: str):
    return session.query(models.topic).filter_by(topic_name=topic_name).one_or_none()



if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    import models as models
    from sqlalchemy import create_engine

    # Create engine at the beginning of the app
    engine = create_database()

    # Create session when new data is required
    session = create_session(engine)

    client1 = create_client("dev1", "111.111", 110)
    client2 = create_client(client_name="dev2", client_ip="222.222", client_port=220)

    message1 = create_message(message="Bel", temp=24.5, is_home=0)
    message2 = create_message(message="Al", temp=21.3, is_home=1)

    topic1 = create_topic(topic_name="Topic1", messages=[message1, message2], clients=[client1, client2])

    session.add(topic1)
    session.commit()

    getTopic = get_topic_by_name_first(topic_name="Topic1")

    print("Topic ---> ", getTopic)
    print("Messages ---> ", getTopic.messages)
    print("Message 0 ---> ", getTopic.messages[0])
    print("Clients ---> ", getTopic.clients)
    print("Client 0 ---> ", getTopic.clients[0])
