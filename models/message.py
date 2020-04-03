# from typing import NamedTuple

class message:
    def __init__(self, messageID: int, userInfo: object, sourceDeviceInfo: object):
        self.messageID = messageID
        self.userInfo = userInfo
        self.sourceDeviceInfo = sourceDeviceInfo

    def asDict(self):
        return dict(messageID=self.messageID, userInfo=self.userInfo, sourceDeviceInfo=self.sourceDeviceInfo)


def asMessage(dic):
    return message(dic["messageID"], dic["userInfo"], dic["sourceDeviceInfo"])
