from models.user import User
from models import Modellable
from context import Context


class UserBoard(Modellable, Context):
    def __init__(self):
        super().__init__()

    def clone(self):
        return UserBoard()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "board_id": self.object_id
        }
