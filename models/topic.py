from models.base import *


class topic(Base):
    __tablename__ = "topic"

    topic_id = Column(Integer, primary_key=True, autoincrement=True)
    topic_name = Column(String)
    # message_id = Column(Integer)
    # client_id = Column(Integer)
    messages = relationship("message", back_populates="topic")
    clients = relationship("client", back_populates="topic")

    def __repr__(self):
        return "<topic(topic_id={}, topic_name={})>".format(self.topic_id, self.topic_name)
