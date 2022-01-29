from .state import State


class FinalState(State):
    def __init__(self, t):
        super().__init__()
        self.type = t