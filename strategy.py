

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def perform_query(self, user_id, object_id, payload):
        raise NotImplementedError
