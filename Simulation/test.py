from Simulation.agent import Agent
from Simulation.environment import Environment
from Simulation.parameter import Parameter
from Simulation.activation_rule import ActivationRule
from main import main

from TreatmentTree.tree_draw import print_graph, print_console_nodes, print_best_branch

class Tos(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=2) -> None:
        super().__init__('tos', activation_rules, 72, 2)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('tos') != None:
                env.update_parameter('tos', 0.4)
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', -0.5)
        return env

class Fiebre(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=4) -> None:
        super().__init__('fiebre', activation_rules, 72, 4)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('fiebre') != None:
                env.update_parameter('fiebre', 1)
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', -4)
        return env

class DolorCabeza(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=2) -> None:
        super().__init__('dolor de cabeza', activation_rules, 36, 2)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('dolor de cabeza') != None:
                env.update_parameter('dolor de cabeza', 4)
        return env

class Dipirona(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=8) -> None:
        super().__init__('dipirona', activation_rules, 24, 8)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('dolor de cabeza') != None:
                env.update_parameter('dolor de cabeza', -4)
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
                env.update_parameter('fiebre', -1)
        return env

class Calbamol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=6) -> None:
        super().__init__('calbamol', activation_rules, 48, 6)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('dolor de cabeza') != None:
                env.update_parameter('dolor de cabeza', -2)
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
                env.update_parameter('fiebre', -0.5)
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', 3)
        return env

class Antibiotico(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('antibiotico', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>37:
                env.update_parameter('fiebre', -2)
            if env.get_parameter('tos') != None:
                env.update_parameter('tos', -10)
        return env

class Plaquetol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=8) -> None:
        super().__init__('plaquetol', activation_rules, 24, 8)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        if time > 0:
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', 2)
        return env


tos_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,22)}, time_condition=(0,1e9))
tos = Tos(name="tos",activation_rules=[tos_rule])

dc_rule1 = ActivationRule(parameters_conditions={'tos':(10, 200)}, time_condition=(0,1e9))
dc_rule2 = ActivationRule(parameters_conditions={'fiebre':(37, 200)}, time_condition=(0,1e9) )
dc = DolorCabeza(name='dolor de cabeza',activation_rules=[dc_rule1, dc_rule2])

fiebre_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,15)}, time_condition=(0,1e9))
fiebre = Fiebre(name='fiebre',activation_rules=[fiebre_rule])


antibiotico_rule = ActivationRule(parameters_conditions={'fiebre':(38, 100)}, time_condition=(72,1e9))
antibiotico = Antibiotico(name='antibiotico',activation_rules=[antibiotico_rule])

dipirona_rule1 = ActivationRule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9))
dipirona_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(10, 1000)}, time_condition=(0,1e9))
dipirona =  Dipirona(name='dipirona',activation_rules=[dipirona_rule1, dipirona_rule2])

calbamol_rule1 = ActivationRule(parameters_conditions={'fiebre':(38, 100)}, time_condition=(0,1e9))
calbamol_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(20, 1000)}, time_condition=(48,1e9))
calbamol_rule3 = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 5)}, time_condition=(24,1e9))
calbamol = Calbamol(name='calbamol',activation_rules=[calbamol_rule1, calbamol_rule2, calbamol_rule3])

plaquetol_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 10)}, time_condition=(24,1e9))
plaquetol = Plaquetol(name='plaquetol', activation_rules=[plaquetol_rule])

p_plaqueta = Parameter('plaqueta', value=20, low_good_limit=23, upp_good_limit=50, low_bad_limit=-20, upp_bad_limit=80)
p_tos = Parameter('tos', value=10, low_good_limit=0, upp_good_limit=5, low_bad_limit=0, upp_bad_limit=60)
p_dolorCabeza = Parameter('dolor de cabeza', value=5, low_good_limit=0, upp_good_limit=15, low_bad_limit=0, upp_bad_limit=100)
p_fiebre = Parameter('fiebre', value=36.5, low_good_limit=35, upp_good_limit=36.9, low_bad_limit=34.5, upp_bad_limit=43)

environment = Environment(parameters=[p_dolorCabeza, p_plaqueta, p_tos, p_fiebre])

t_t = main(env=environment, treatment=set([antibiotico, dipirona, calbamol, plaquetol]), disease=set([tos, fiebre, dc]), tick=1, end_time=168, simulations=1000)

print_best_branch(t_t.root)

#print(t_t.root)
#print_console_nodes([t_t.root], 25)

#print_graph(t_t.root, 170)