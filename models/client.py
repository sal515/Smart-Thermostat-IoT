from models.base import *


class client(Base):
    __tablename__ = "client"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String)
    client_ip = Column(String)
    client_port = Column(Integer)
    topic_id = Column(Integer, ForeignKey('topic.topic_id'))

    topic = relationship("topic", back_populates="clients")

    # def __init__(self, client_name: str, client_ip: str, client_port: int):
    #     self.client_name = client_name
    #     self.client_ip = client_ip
    #     self.client_port = client_port

    def __repr__(self):
        return "<client(client_id={}, client_name={}, client_ip={}, client_port={})>".format(self.client_id, self.client_name, self.client_ip, self.client_port)
