class topics_table:
    def __init__(self, id_table: int, topic_name: str, message: str, client_list_id: int):
        self.id_table = id_table
        self.topic_name = topic_name
        self.message = message
        self.client_list_id = client_list_id

    def asDict(self):
        return dict(id_table=self.id_table, topic_name=self.topic_name, message=self.message,
                    client_list_id=self.client_list_id)


def asTopic(dictionary):
    return topics_table(dictionary["id_table"], dictionary["topic_name"], dictionary["message"],
                        dictionary["client_list_id"])
