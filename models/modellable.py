from abc import ABC, abstractmethod


class Modellable:
    @abstractmethod
    def to_dict(self):
        raise NotImplementedError
