from .state import State


class FinalState(State):
    def __init__(self):
        super().__init__()
        self.type = []
