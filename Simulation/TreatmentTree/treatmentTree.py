from .node import Node
from .UCT import UCT

class TreatmentTree(object):
    def __init__(self, value:str):
        self._root:Node = Node(value)
        self._current:Node = self._root
        self._node_count = 0

    @property
    def root(self):
        '''
        Returns the node root of the tree
        '''
        return self._root

    @property
    def node_count(self):
        '''
        Returns the number of nodes in the tree
        '''
        return self._node_count

    def expand_selection(self, _posible_intervention:list[str], current_time)->Node:
        '''
        Based on the possible candidate children of the current node, expand the tree and select 
        the one based on the UTC policy weighting explotation and exploration
        '''
        _candidate_childs = []
        for child in self._current._children:
            if child.value in _posible_intervention and child.created_time == current_time:
                _candidate_childs.append(child)
                _posible_intervention.remove(child.value)
        for intervention in _posible_intervention:
            self._node_count+=1
            self._current._children.append(Node(intervention, self._current, current_time, self.node_count))
            _candidate_childs.append(self._current._children[-1])
        self._current = UCT.find_best_uct(_candidate_childs)
        return self._current

    def back_propagation(self, utility_score):
        '''
        Updates the simulation variables of all ancestors of the current node.
        Increases the visit counter and utility score values of said nodes.
        '''
        while(self._current.parent != None):
            self._current.utility_score += utility_score
            self._current.visit_count += 1
            self._current = self._current.parent
        self._current.utility_score += utility_score
        self._current.visit_count += 1
        return

    def best_branch(self)->list[Node]:
        '''
        Returns a list with the best branch of the tree
        '''
        branch = [] 
        curr = self.root
        def best_child(node:Node)->Node:
            more_p_child = None
            gr_probability = -1e9
            for child in node._children:
                if child.visit_count/node.visit_count > gr_probability:
                    gr_probability = child.visit_count/node.visit_count
                    more_p_child = child
            return more_p_child
        while curr != None:
            branch.append(curr)
            curr = best_child(curr)
        return branch

    def calculate_probability(self):
        '''
        Calculate for each node of the tree its probability value
        '''
        self.root.probability_value = 100.0
        def __calculate(nodes:list[Node]):
            if len(nodes) == 0:
                return
            for node in nodes:
                if node is not None:
                    node.probability_value = round((node.visit_count/node.parent.visit_count)*100,1)
            childrens = []
            for node in nodes:
                if node is not None:
                    childrens.extend(node._children)
            __calculate(childrens)
        __calculate(self.root._children)

    def prunning(self, max_childs=2, acc_probability=75, low_level_exclusion=30):
        '''
        Prune the tree keeping the maximum number of children specified by "max_childs" or 
        those that accumulate the highest probability equal to "acc_probability".
        Starting from the second level, prune among the children those that have a % lower 
        than low_level_exclusion
        '''
        self.root.probability_value=100.0
        def best_childs(node:Node, max_childs, acc_probability, make_exclusion, exclusion)->list[Node]:
            childs = []
            acc_p = 0
            for child in node._children:
                childs.append(child)
            childs = sorted(childs, key=lambda x: x.probability_value, reverse=True)
            limit = min(max_childs, len(childs))
            i = 0
            while acc_p < acc_probability and i < limit:
                acc_p += childs[i].probability_value
                i+=1
            prunning_childs = []
            if make_exclusion and i>=1:
                prunning_childs = [childs[0]] 
                prunning_childs.extend([n for n in childs[1:i] if n.probability_value>exclusion])
            return prunning_childs if make_exclusion else childs[:i]
        def prunning_rec(nodes:list[Node], max_childs, acc_p, make_exclusion, exclusion):
            if len(nodes) == 0:
                return
            for node in nodes:
                node._children = best_childs(node, max_childs, acc_p, make_exclusion, exclusion)
            for node in nodes:
                prunning_rec(node._children, max_childs, acc_p, True, exclusion)
        prunning_rec([self.root], max_childs, acc_probability, False, low_level_exclusion)