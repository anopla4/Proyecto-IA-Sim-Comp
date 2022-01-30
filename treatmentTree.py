from node import Node
from UCT import UCT
from random import random

class TreatmentTree(object):
    def __init__(self, value:str, max_time : int = 10):
        self._root:Node = Node(value)
        #self.actions = actions
        self._current:Node = self._root
        self.max_time = max_time

    @property
    def root(self):
        return self._root

    def expand_selection(self, _posible_intervention:list[str])->Node:
        _candidate_childs = []
        for child in self._current._children:
            if child.value in _posible_intervention:
                _candidate_childs.append(child)
                _posible_intervention.remove(child.value)
        for int in _posible_intervention:
            self._current._children.append(Node(int))
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