from userboard import UserBoard
from context import Context


class ContextFactory:
    """Factory + Prototype"""

    __prototypes = {
        "userboard": UserBoard()
    }

    def create_context(self, what) -> Context:
        return self.__prototypes[what].clone()
