from State import State
from Node import Node
from Action import Action
from UCT import UCT
from fuzy_engine import fuzy_engine

class MCTS(object):
    def __init__(self, state : State, actions : list[Action]):
        self.root = Node(state)
        self.actions = actions

    def find_next_Action(self):
        pass

    def selection(self):
        node = self.root
        while(node.children):
            node = UCT.find_best_utc(node)
        return node
    
    def expand(self, node : Node):
        for action in self.actions:
            node.children.append(Node(fuzy_engine(node.state, action), parent = node))
    
    def simulate_playout(self,node : Node):
        pass

    def back_propagation(self, node, utility_score):
        while(node.parent != None):
            node.utility_score = utility_score
            node = node.parent
        node.utility_score = utility_score
        return


        

    

