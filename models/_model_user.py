
from peewee import *
from ._model_basemodel import BaseModel


class UserModel(BaseModel):
    username = CharField()
