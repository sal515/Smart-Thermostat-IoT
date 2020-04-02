# from typing import NamedTuple

class deviceInfo:
    def __init__(self, deviceID: int, deviceIP: str, deviceURL: str):
        self.deviceID = deviceID
        self.deviceIP = deviceIP
        self.deviceURL = deviceURL

    def asDict(self):
        return dict(deviceID=self.deviceID, deviceIP=self.deviceIP, deviceURL=self.deviceURL)


def asUserInfo(dic):
    return deviceInfo(dic["deviceID"], dic["deviceIP"], dic["deviceURL"])
