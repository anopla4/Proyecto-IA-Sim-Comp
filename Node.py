from State import State

class Node(object):
    def __init__(self,state : State, parent : Node = None):
        self.state = state
        self.parent = parent
        self.children = list[Node]
        self.visit_count = 0
        self.utility_score = 0
