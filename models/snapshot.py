from abc import ABC, abstractmethod


class Snapshot(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_date(self) -> str:
        raise NotImplementedError
