from models.base import *
import datetime


class message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())
    topic_id = Column(Integer, ForeignKey('topic.topic_id'))

    topic = relationship("topic", back_populates="messages")

    def __repr__(self):
        return "<message(message_id={}, message={}, createdAt={})>".format(self.message_id, self.message, self.create_date)
