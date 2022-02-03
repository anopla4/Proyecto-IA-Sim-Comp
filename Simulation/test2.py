from Simulation.agent import Agent
from Simulation.environment import Environment
from Simulation.parameter import Parameter
from Simulation.rule import Rule
from main import main
from TreatmentTree.node import Node

#import networkx as nx
#import matplotlib.pyplot as plt
from TreatmentTree.tree_draw import print_graph

def print_nodes(nodes:list[Node], n):
    if n== 0 or len(nodes) == 0:
        return
    for node in nodes:
        if node is not None:
            val = node.name ##node.value if node.value!="" else str(n)
            print(val, end="  ")
    print()
    children = []
    for node in nodes:
        if node is not None:
            children.extend(node._children)
    print_nodes(children,n-1)

class E(Agent):
    def __init__(self, name: str, activation_rules, efect_time=168, repetition=1) -> None:
        super().__init__('enf', activation_rules, 168, 1)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('enf') != None:
                env.upadate_parameter('enf', 1)
        return env

class T(Agent):
    def __init__(self, name: str, activation_rules, efect_time=20, repetition=4) -> None:
        super().__init__('trat', activation_rules, 20, 4)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('trat') != None:
                env.upadate_parameter('trat', 1)
        return env

e_rule = Rule(parameters_conditions={'param':(-1e9,1e9)}, time_condition=(0,1e9), then='enf')
e = E(name="enf",activation_rules=[e_rule])

t_rule = Rule(parameters_conditions={'param':(-1e9,1e9)}, time_condition=(0,1e9), then='trat')
t = T(name="trat",activation_rules=[t_rule])

p = Parameter('param', value=0, inf_limit=-1e9, upper_limit=1e9)
enf_p = Parameter('enf', value=0, inf_limit=-1e9, upper_limit=1e9)
trat_p = Parameter('trat', value=0, inf_limit=-1e9, upper_limit=1e9)

environment = Environment(parameters=[p, enf_p, trat_p])

t_t = main(env=environment, treatment=set([t]), disease=set([e]), tick=1, end_time=168, simulations=2)

print_nodes([t_t.root], 25)

##print_graph(t_t.root, 25)