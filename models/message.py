from models.base import *
import datetime

class message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    temp = Column(Float)
    is_home = Column(Integer)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())
    topic_id = Column(Integer, ForeignKey('topic.topic_id'))

    topic = relationship("topic", back_populates="messages")

    def __repr__(self):
        return "<message(message_id={}, name={}, temp={}, is_home={}, createdAt={})>".format(self.message_id, self.name, self.temp, self.is_home, self.create_date)
