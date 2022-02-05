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
                    then=("increse","a lot")))
                actions_rules.append(Rule(
                    {'tos':'baja'},
                then=("tos","media")))
                actions_rules.append(Rule(
                    {'tos': 'media',},
                then=("tos","alta")))
                actions_rules.append(Rule(
                    {'plaqueta':'estable'},
                    then=("plaqueta","baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'muy alta'},
                    then=("plaqueta","alta")))
                actions_rules.append(Rule(
                    {'plaqueta':'baja'},
                    then=("plaqueta","muy baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'muy baja'},
                    then=("plaqueta","muy baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'alta'},
                    then=("plaqueta","estable")))
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
                    {'temperatura':'baja'},
                then=("temperatura","media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=("temperatura","alta")))
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=("temperatura","muy alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=("temperatura","muy alta")))

                actions_rules.append(Rule(
                    {'plaqueta':'estable'},
                    then=("plaqueta","baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'muy alta'},
                    then=("plaqueta","alta")))
                actions_rules.append(Rule(
                    {'plaqueta':'baja'},
                    then=("plaqueta","muy baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'muy baja'},
                    then=("plaqueta","muy baja")))
                actions_rules.append(Rule(
                    {'plaqueta':'alta'},
                    then=("plaqueta","estable")))

                actions_rules.append(Rule(
                    {'dolor de cabeza':'bajo'},
                    then=("dolor de cabeza","medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                    then=("dolor de cabeza","alto")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                    then=("dolor de cabeza","alto")))
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
                    {'dolor de cabeza':'bajo'},
                    then=("dolor de cabeza","medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                    then=("dolor de cabeza","alto")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                    then=("dolor de cabeza","alto")))
        # else:
        #     if env.get_parameter('dolor de cabeza') != None:
        #         actions_rules.append(Rule(
        #             {'dolor de cabeza':'bajo'},
        #             then=("dolor de cabeza","alto")))
        #         actions_rules.append(Rule(
        #             {'dolor de cabeza':'medio'},
        #             then=("dolor de cabeza","alto")))
        return actions_rules