# from typing import NamedTuple

class userInfo:
    def __init__(self, name: str, temp: int, isHome: bool):
        self.name = name
        self.temp = temp
        self.isHome = isHome

    def asDict(self):
        return dict(name=self.name, temp=self.temp, isHome=self.isHome)


def asUserInfo(dic):
    return userInfo(dic["name"], dic["temp"], dic["isHome"])
