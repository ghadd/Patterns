from strategy import Strategy
from models import BoardModel, UserModel


class AddTaskStrategy(Strategy):
    def perform_query(self, user_id, object_id, payload):
        user = UserModel.get(user_id)
        board = BoardModel.get(object_id)

        try:
            board.add_task_from(user, payload['task'])
            print('[PERMITTED]', 'New task: ', payload['task'])
        except ValueError as e:
            print("[NOT PERMITTED]", e)
