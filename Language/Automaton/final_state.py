from .State import State


class FinalState(State):
    def __init__(self, state = None, t = None):
        super().__init__(state)
        self.type = t
