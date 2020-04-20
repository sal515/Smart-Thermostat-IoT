class user_info_table:
    def __init__(self, client_list_id: int, client_id: int):
        self.client_list_id = client_list_id
        self.client_id = client_id

    def asDict(self):
        return dict(client_list_id=self.client_list_id, client_id=self.client_id)


def asUserInfo(dic):
    return user_info_table(dic["client_list_id"], dic["client_id"])
