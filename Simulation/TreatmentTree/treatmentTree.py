from .node import Node
from .UCT import UCT

class TreatmentTree(object):
    def __init__(self, value:str):
        self._root:Node = Node(value)
        self._current:Node = self._root
        self._node_count = 0

    @property
    def root(self):
        return self._root

    @property
    def node_count(self):
        return self._node_count

    def expand_selection(self, _posible_intervention:list[str], current_time)->Node:
        _candidate_childs = []
        for child in self._current._children:
            if child.value in _posible_intervention and child.created_time == current_time:
                _candidate_childs.append(child)
                _posible_intervention.remove(child.value)
        for intervention in _posible_intervention:
            self._node_count+=1
            self._current._children.append(Node(intervention, self._current, current_time, self.node_count))
            _candidate_childs.append(self._current._children[-1])
        self._current = UCT.find_best_utc(_candidate_childs)
        return self._current

    def back_propagation(self, utility_score):
        while(self._current.parent != None):
            self._current.utility_score += utility_score
            self._current.visit_count += 1
            self._current = self._current.parent
        self._current.utility_score += utility_score
        self._current.visit_count += 1
        return

    def best_branch(self):
        pass