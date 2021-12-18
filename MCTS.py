from State import State
from Node import Node
from Action import Action
from UCT import UCT
from fuzy_engine import fuzy_engine
from random import random
import time

class MCTS(object):
    def __init__(self, state : State, actions : list[Action], max_time : int = 10):
        self.root = Node(state)
        self.actions = actions
        self.max_time = max_time

    def find_next_Action(self):
        init = time.time()
        while(time.time() - init < self.max_time):
            node = self.selection()
            self.simulate_playout(node)
        best_visit_number = 0
        action = None
        for child in ((self.root).children):
            if child.visit_count >= best_visit_number:
                best_visit_number = child.visit_count
                action = child.action
        return action 

    def selection(self):
        node = self.root
        while(node.children):
            node = UCT.find_best_utc(node)
        return node
    
    def expand(self, node : Node):
        for action in self.actions:
            node.children.append(Node(fuzy_engine(node.state, action), parent = node, action = action))
    
    def simulate_playout(self,node : Node):
        is_terminal = node.state.IsTerminal()
        state = node.state
        while (is_terminal == -1):
            state = MCTS.select_random_action(state, self.actions)
            is_terminal = state.IsTerminal()
        self.back_propagation(node, is_terminal)
        

    def back_propagation(self, node, utility_score):
        while(node.parent != None):
            node.utility_score += utility_score
            node.visit_count += 1
            node = node.parent
        node.utility_score = utility_score
        return
    
    @staticmethod
    def select_random_action(state, actions):
        index_action = random() * len(actions)
        return fuzy_engine(state, actions[index_action])        


        

    

