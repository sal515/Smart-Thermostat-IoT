# from typing import NamedTuple

class topic:
    def __init__(self, topic: str, subscribers: [] = [], publishers: [] = [], messages: [] = []):
        self.topic = topic
        self.subscribers = subscribers
        self.publishers = publishers
        self.messages = messages

    def asDict(self):
        return dict(topic=self.topic, subscribers=self.subscribers, publishers=self.publishers, messages=self.messages)


def asTopic(dictionary):
    return topic(dictionary["topic"], dictionary["subscribers"], dictionary["publishers"], dictionary["messages"])
