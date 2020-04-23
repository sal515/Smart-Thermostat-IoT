import json
from json import JSONEncoder as jsonEncoder


class encoder(jsonEncoder):
    def default(self, o):
        return o.__dict__
