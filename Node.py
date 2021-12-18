from State import State
from Action import Action

class Node(object):
    def __init__(self,state : State, parent : Node = None, action : Action = None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visit_count = 0
        self.utility_score = 0
        self.action = action
