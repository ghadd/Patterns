from abc import ABC
from .board import Board


class BoardMeta(ABC, Board):
    def __init__(self, decorated_board):
        self.decorated_board = decorated_board


class BackgroundMeta(BoardMeta):
    def __init__(self, decorated_board, background):
        super().__init__(decorated_board)

        bg_url = background
        self.decorated_board.background = bg_url

    def to_dict(self):
        return super().to_dict() | {
            "background": self.decorated_board.background
        }
