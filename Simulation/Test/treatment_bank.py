from Simulation.agent import Agent
from Simulation.environment import Environment
from FuzzyEngine.rule import Rule
from random import random

class DipironaSimple(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=8) -> None:
        super().__init__('dipirona 1', activation_rules, 24, 8)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.7:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                parameters_conditions={'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrese',"low")))
                actions_rules.append(Rule(
                parameters_conditions= {'dolor de cabeza':'alto'},
                param_destination='dolor de cabeza',
                then=('decrese',"medium")))
                actions_rules.append(Rule(
                    parameters_conditions= {'dolor de cabeza':'bajo'},
                param_destination='dolor de cabeza',
                then=('decrese',"low")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                 parameters_conditions= {'temperatura':'alta'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'baja'},
                param_destination='temperatura',
                then=('decrease',"low")))
        return actions_rules

class DipironaDoble(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('dipirona 2', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules= []
        if r < 0.50:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                parameters_conditions= {'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrease',"low")))
                actions_rules.append(Rule(
                  parameters_conditions= {'dolor de cabeza':'alto'},
                param_destination='dolor de cabeza',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'dolor de cabeza':'bajo'},
                param_destination='dolor de cabeza',
                then=('decrease',"low")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                 parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                  parameters_conditions= {'temperatura':'alta'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                  parameters_conditions= {'temperatura':'media'},
                param_destination='temperatura',
                then=('decrease',"medium")))
        return actions_rules

class Calbamol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=6) -> None:
        super().__init__('calbamol', activation_rules, 48, 6)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.40:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                 parameters_conditions={'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrese',"low")))
                actions_rules.append(Rule(
                 parameters_conditions={'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrese',"high")))
                actions_rules.append(Rule(
                  parameters_conditions={'dolor de cabeza':'bajo'},
                param_destination='dolor de cabeza',
                then=('decrese',"low")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                parameters_conditions={'temperatura':'muy alta'},
                param_destination="temperatura",
                then=('decrease',"high")))
                actions_rules.append(Rule(
                   parameters_conditions={'temperatura':' alta'},
                param_destination="temperatura",
                then=('decrease',"high")))
                actions_rules.append(Rule(
                 parameters_conditions={'temperatura':'media'},
                param_destination="temperatura",
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                  parameters_conditions={'temperatura':'muy alta'},
                param_destination="temperatura",
                then=('increase',"medium")))
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'muy baja'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'baja'},
                param_destination='plaqueta',
                then=('increase',"high")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'muy alta'},
                param_destination='plaqueta',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'alta'},
                param_destination='plaqueta',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                 parameters_conditions={'plaqueta' : 'estable'},
                param_destination='plaqueta',
                then=('increase',"medium")))
        elif r < 0.80:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                parameters_conditions= {'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                 parameters_conditions= {'dolor de cabeza':'alto'},
                param_destination='dolor de cabeza',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'dolor de cabeza':'bajo'},
                param_destination='dolor de cabeza',
                then=('decrease',"low")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':' alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'media'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                 parameters_conditions= {'temperatura':'baja'},
                param_destination='temperatura',
                then=('decrease',"low")))
        return actions_rules

class Jarabe(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=12) -> None:
        super().__init__('jarabe', activation_rules, 48, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.75:
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'baja'},
                param_destination='tos',
                then=('decrease',"low")))
                actions_rules.append(Rule(
                 parameters_conditions= {'tos':'media'},
                param_destination='tos',
                then=('decrease',"low")))
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'alta'},
                param_destination='tos',
                then=('decrease',"high")))
        return actions_rules

class Antibiotico(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=12) -> None:
        super().__init__('antibiotico', activation_rules, 36, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.5:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
               parameters_conditions= {'temperatura':' alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
               parameters_conditions= {'temperatura':'media'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'baja'},
                param_destination='temperatura',
                then=('decrease',"low")))
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
               parameters_conditions= {'tos':'baja'},
                param_destination='tos',
                then=('decrease',"low")))
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'media'},
                param_destination='tos',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'alta'},
                param_destination='tos',
                then=('decrease',"high")))
        if r < 0.8:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'media'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'baja'},
                param_destination='temperatura',
                then=('decrease',"low")))
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'baja'},
                param_destination='tos',
                then=('decrease',"low")))
                actions_rules.append(Rule(
                parameters_conditions= {'tos':'media'},
                param_destination='tos',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                 parameters_conditions= {'tos':'alta'},
                param_destination='tos',
                then=('decrease',"high")))
        else:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                 parameters_conditions= {'temperatura':'muy alta'},
                param_destination='temperatura',
                then=('decrease',"high")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'alta'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'media'},
                param_destination='temperatura',
                then=('decrease',"medium")))
                actions_rules.append(Rule(
                parameters_conditions= {'temperatura':'baja'},
                param_destination='temperatura',
                then=('decrease',"low")))
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'muy baja'},
                param_destination='plaqueta',
                then=('increase',"high")))
                actions_rules.append(Rule(
                 parameters_conditions={'plaqueta' : 'baja'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'alta' : 'baja'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'estable'},
                param_destination='plaqueta',
                then=('increase',"high")))
                actions_rules.append(Rule(
                 parameters_conditions={'plaqueta' : 'alta'},
                param_destination='plaqueta',
                then=('increase',"low")))
        return actions_rules

class Plaquetol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('plaquetol', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.7:
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'muy baja'},
                param_destination='plaqueta',
                then=('increase',"high")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'baja'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'alta'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'estable'},
                param_destination='plaqueta',
                then=('increase',"medium")))
                actions_rules.append(Rule(
                parameters_conditions={'plaqueta' : 'estable'},
                param_destination='plaqueta',
                then=('increase',"low")))
        return actions_rules