# from typing import NamedTuple

class deviceInfo:
    def __init__(self, deviceID: int, deviceIP: str, deviceURL: str, sub_topics: [] = [], pub_topics: [] = []):
        self.deviceID = deviceID
        self.deviceIP = deviceIP
        self.deviceURL = deviceURL
        self.sub_topics = sub_topics
        self.pub_topics = pub_topics

    def asDict(self):
        return dict(deviceID=self.deviceID, deviceIP=self.deviceIP, deviceURL=self.deviceURL,
                    sub_topics=self.sub_topics, pub_topics=self.pub_topics)


def asUserInfo(dic):
    return deviceInfo(dic["deviceID"], dic["deviceIP"], dic["deviceURL"], dic["sub_topics"], dic["pub_topics"])
