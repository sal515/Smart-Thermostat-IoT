from models.base import *


class message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    temp = Column(Float)
    is_home = Column(Integer)
    topic_id = Column(Integer, ForeignKey('topic.topic_id'))

    topic = relationship("topic", back_populates="messages")

    def __repr__(self):
        return "<message(message_id={}, name={}, temp={}, is_home={})>".format(self.message_id, self.name, self.temp, self.is_home)
