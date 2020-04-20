class clients_table:
    def __init__(self, client_id: int, client_device_name: str, client_ip: int, client_port: int):
        self.client_id = client_id
        self.client_device_name = client_device_name
        self.client_ip = client_ip
        self.client_port = client_port

    def asDict(self):
        return dict(client_id=self.client_id, client_device_name=self.client_device_name, client_ip=self.client_ip,
                    client_port=self.client_port)


def asUserInfo(dic):
    return clients_table(dic["client_id"], dic["client_device_name"], dic["client_ip"], dic["client_port"])
