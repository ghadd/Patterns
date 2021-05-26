from abc import abstractmethod
from strategy import Strategy


class Context(object):
    def __init__(self, user_id=None, object_id=None, payload: dict = None, strategy: Strategy = None):
        self.user_id = user_id
        self.object_id = object_id
        self._payload = payload or {}
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def payload(self) -> dict:
        return self._payload

    @payload.setter
    def payload(self, payload: dict):
        self._payload = payload

    def exec(self):
        assert self._strategy is not None
        self._strategy.perform_query(
            self.user_id, self.object_id, self._payload)

    @abstractmethod
    def clone(self):
        raise NotImplementedError
