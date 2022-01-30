class Node(object):
    def __init__(self, value:str, parent = None):
        self._value:str = value
        self._states = []
        self._parent:Node = parent
        self._children:list[Node] = []
        self._visit_count:int = 0
        self._utility_score = 0

    @property
    def value(self)->str:
        return self._value

    @property
    def states(self):
        return self._states

    @property
    def intervention(self):
        return self._value

    def empty(self)->bool:
        return self._value == ""