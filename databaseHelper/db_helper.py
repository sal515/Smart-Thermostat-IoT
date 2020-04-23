from sqlalchemy.orm import sessionmaker
import models as models
from sqlalchemy import create_engine


def create_database():
    # Create tables if doesn't exist using base and engine
    engine = create_engine('sqlite:///iot.db', echo=True)
    models.Base.metadata.create_all(engine)
    return engine


def create_session(engine):
    # Store objects to db using sessions
    Session = sessionmaker(bind=engine)
    return Session()


def create_client(client_name: str, client_ip: str, client_port: int):
    return models.client(client_name=client_name, client_ip=client_ip, client_port=client_port)


def create_message(name: str, temp: float, is_home: int):
    return models.message(name=name, temp=temp, is_home=is_home)


def create_topic(topic_name: str, messages: [], clients: []):
    return models.topic(topic_name=topic_name, messages=messages, clients=clients)


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

    message1 = create_message(name="Bel", temp=24.5, is_home=0)
    message2 = create_message(name="Al", temp=21.3, is_home=1)

    topic1 = create_topic(topic_name="Topic1", messages=[message1, message2], clients=[client1, client2])

    session.add(topic1)
    session.commit()

    getTopic = session.query(models.topic).filter_by(topic_name="Topic1").first()
    print("Topic ---> ", getTopic)
    print("Messages ---> ", getTopic.messages)
    print("Message 0 ---> ", getTopic.messages[0])
    print("Clients ---> ", getTopic.clients)
    print("Client 0 ---> ", getTopic.clients[0])
