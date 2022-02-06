from Simulation.agent import Agent
from Simulation.environment import Environment
from FuzzyEngine.rule import Rule
from random import random

class Tos(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=3) -> None:
        super().__init__('tos', activation_rules, 72, 3)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.8:
            if env.get_parameter('tos') != None:
                actions_rules.append(Rule(
                    parameters_conditions={'tos':'alta',
                                    'plaqueta':'baja'},
                    param_destination='tos',
                    then=("increase","low")))
                actions_rules.append(Rule(
                    parameters_conditions={'tos':'baja',
                                           'plaqueta':'estable'},
                    param_destination='tos',
                    then=("increase","medium")))
                actions_rules.append(Rule(
                   parameters_conditions= {'tos': 'media',
                                           'plaqueta':'alta'},
                   param_destination='tos',
                   then=('decrease','high')))
                actions_rules.append(Rule(
                   parameters_conditions= {'tos':'alta',
                                'plaqueta':'muy alta'},
                   param_destination='tos',
                    then=("decrease","high")))
                actions_rules.append(Rule(
                    parameters_conditions={'tos':'media','plaqueta':'muy alta'},
                    param_destination='tos',
                    then=("decrease","high")))
                actions_rules.append(Rule(
                    parameters_conditions={'plaqueta':'estable',
                                           'tos':'alta'},
                    param_destination='plaqueta',
                    then=("decrease","medium")))
                actions_rules.append(Rule(
                    parameters_conditions={'tos':'alta',
                        'plaqueta':'baja'},
                    param_destination='plaqueta',
                    then=("decrease"," high")))
                actions_rules.append(Rule(
                    parameters_conditions={'plaqueta':'alta',
                                           'tos':'alta'},
                    param_destination='plaqueta',
                    then=("decrease","high")))
        return actions_rules

class Fiebre(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=4) -> None:
        super().__init__('fiebre', activation_rules, 72, 4)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.75:
            if env.get_parameter('temperatura') != None:
                actions_rules.append(Rule(
                    parameters_conditions= {'temperatura':'baja',
                                            'plaqueta':'baja'},
                    param_destination='temperatura',
                    then=("increase","medium")))
                actions_rules.append(Rule(
                    parameters_conditions={'temperatura':'baja',
                                           'plaqueta':'baja'},
                    param_destination='plaqueta',
                then=("increase","high")))
                actions_rules.append(Rule(
                    parameters_conditions={'temperatura':'muy alta',
                                           'plaqueta':'muy alta'},
                    param_destination='tos',
                then=("decrease","high")))
                actions_rules.append(Rule(
                   parameters_conditions= {'temperatura':'alta',
                                           'plaqueta':'alta'},
                   param_destination='temperatura',
                then=("decrease","medium")))

                actions_rules.append(Rule(
                   parameters_conditions= {'plaqueta':'estable',
                                           'temperatura':'alta'},
                   param_destination='plaqueta',
                    then=("increase","low")))
                actions_rules.append(Rule(
                    parameters_conditions={'plaqueta':'muy alta',
                                           'temperatura':'media'},
                    param_destination='temperatura',
                    then=("decrease","high")))

                actions_rules.append(Rule(
                    parameters_conditions={'dolor de cabeza':'bajo',
                                           'plaqueta':'baja'},
                    param_destination='dolor de cabeza',
                    then=("increase","medium")))
                actions_rules.append(Rule(
                    parameters_conditions={'dolor de cabeza':'medio',
                                           'plaqueta':'muy alta'},
                    param_destination='dolor de cabeza',
                    then=("decrease","high")))
                actions_rules.append(Rule(
                    parameters_conditions={'dolor de cabeza':'alto',
                                           'plaqueta':'muy alta'},
                    param_destination='dolor de cabeza',
                    then=("decrease","high")))
        return actions_rules

class DolorCabeza(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=4) -> None:
        super().__init__('dolor de cabeza', activation_rules, 36, 4)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.75:
            if env.get_parameter('dolor de cabeza') != None:
                actions_rules.append(Rule(
                    parameters_conditions= {'dolor de cabeza':'bajo'},
                    param_destination='dolor de cabeza',
                    then=("decrease","medium")))
                actions_rules.append(Rule(
                    parameters_conditions={'dolor de cabeza':'medio'},
                    param_destination='dolor de cabeza',
                    then=("increase","low")))
        # else:
        #     if env.get_parameter('dolor de cabeza') != None:
        #         actions_rules.append(Rule(
        #             {'dolor de cabeza':'bajo'},
        #             then=("dolor de cabeza","alto")))
        #         actions_rules.append(Rule(
        #             {'dolor de cabeza':'medio'},
        #             then=("dolor de cabeza","alto")))
        return actions_rules