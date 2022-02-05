from .state import State


class FinalState(State):
    def __init__(self, t=None):
        if t == None:
            self.type = set()
        else:
            self.type = t
