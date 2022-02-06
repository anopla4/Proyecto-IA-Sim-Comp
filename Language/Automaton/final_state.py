from .state import State


class FinalState(State):
    def __init__(self, state=None, t=None):
        self.state = state
        if t == None:
            self.type = set()
        else:
            self.type = t
