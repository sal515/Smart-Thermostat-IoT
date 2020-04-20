class user_info_table:
    def __init__(self, name: str, temp: int, isHome: bool):
        self.name = name
        self.temp = temp
        self.isHome = isHome

    def asDict(self):
        return dict(name=self.name, temp=self.temp, isHome=self.isHome)

def asUserInfo(dic):
    return user_info_table(dic["name"], dic["temp"], dic["isHome"])
