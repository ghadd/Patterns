from models import *


class DBManager:
    """"Singleton + Proxy"""

    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DBManager.__instance is None:
            DBManager.__instance = DBManager()
        return DBManager.__instance

    def create_schema(self):
        self.database.create_tables([UserModel, BoardModel, UserBoardModel])

    def __init__(self):
        """ Virtually private constructor. """
        if DBManager.__instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            self.database = db
            DBManager.__instance = self
