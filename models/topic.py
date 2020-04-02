# from typing import NamedTuple

class topic:
    def __init__(self, subscribers: [] = [], publishers: [] = [], messages: [] = []):
        self.subscribers = subscribers
        self.publishers = publishers
        self.messages = messages

    def asDict(self):
        return dict(subscribers=self.subscribers, publishers=self.publishers, messages=self.messages)


def asUserInfo(dic):
    return topic(dic["subscribers"], dic["publishers"], dic["messages"])
