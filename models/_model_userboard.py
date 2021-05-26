from peewee import ForeignKeyField
from ._model_basemodel import BaseModel
from ._model_user import UserModel
from ._model_board import BoardModel


class UserBoardModel(BaseModel):
    user_id = ForeignKeyField(UserModel)
    board_id = ForeignKeyField(BoardModel)
