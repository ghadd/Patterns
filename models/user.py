from .modellable import Modellable


class User(Modellable):
    def __init__(self, **kwargs):
        username = kwargs.get('username') or 'unknown'

        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    def to_dict(self):
        return {
            "username": self.username
        }
