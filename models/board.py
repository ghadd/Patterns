from .modellable import Modellable


class Board(Modellable):
    """"Facade"""

    def __init__(self, **kwargs):
        tasks = kwargs.get('tasks') or []
        repo = kwargs.get('repo')

        assert type(tasks) == list

        self.__tasks = tasks
        self.__repo = repo

    def add_task(self, task):
        self.__tasks.append(task)

    def to_dict(self):
        if type(self) != Board:
            self = self.decorated_board

        return {
            "tasks": self.__tasks,
            "repo": self.__repo,
        }
