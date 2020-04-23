from sqlalchemy.orm import sessionmaker
import models as models
from sqlalchemy import create_engine

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    import models as models
    from sqlalchemy import create_engine

    # Create tables if doens't exist using base and engine
    engine = create_engine('sqlite:///iot.db', echo=True)
    models.Base.metadata.create_all(engine)

    # Store objects to db using sessions
    Session = sessionmaker(bind=engine)
    session = Session()

    client1 = models.client(client_name="dev1", client_ip="111.111", client_port=110)
    client2 = models.client(client_name="dev2", client_ip="222.222", client_port=220)

    message1 = models.message(name="Josh", temp=24.5, is_home=0)
    message2 = models.message(name="Al", temp=21.3, is_home=1)

    topic1 = models.topic(topic_name="Topic1", messages=[message1, message2], clients=[client1, client2])

    # session.add(client1)
    # session.add(client2)

    # session.add(topic1)
    # session.commit()

    getTopic = session.query(models.topic).filter_by(topic_name="Topic1").first()

    print(getTopic)
    print(getTopic.messages)
    print(getTopic.clients)
