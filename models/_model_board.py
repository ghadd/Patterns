from models.board import Board
from peewee import CharField, Value
from ._model_basemodel import BaseModel, JSONField
from .snapshot import Snapshot
from .tasks_snapshot import TasksSnapshot
import json


class BoardModel(BaseModel):
    tasks = JSONField()
    repo = CharField(null=True)

    def add_task_from(self, user, task):
        if user.username == "cool_username":
            self.tasks.append(task)
            self.save()
        else:
            raise ValueError("Your username is not cool enough.")

    def save_snapshot(self) -> Snapshot:
        """
        Saves the current state inside a memento.
        """

        return TasksSnapshot(json.dumps(self.tasks))

    def restore_snapshot(self, memento: Snapshot) -> None:
        """
        Restores the Originator's state from a memento object.
        """

        self.tasks = json.loads(memento.get_state())
        self.save()
        print(f"Originator: My state has changed to: {self.tasks}")
