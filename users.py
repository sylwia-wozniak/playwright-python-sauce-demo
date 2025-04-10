import json


class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)


USERS = DictObject.from_dict({
    'user': {
        'username': 'standard_user',
        'password': 'secret_sauce'
    }
})
