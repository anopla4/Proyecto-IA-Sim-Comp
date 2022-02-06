from Simulation.agent import Agent
from Simulation.environment import Environment
from FuzzyEngine.rule import Rule
from random import random

class DipironaSimple(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=4) -> None:
        super().__init__('dipirona 1', activation_rules, 24, 4)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.7:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>37:
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                    destination='temperatura',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                    destination='temperatura',
                    then=('decrease','medium')))
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                    destination='temperatura',
                    then=('decrease','high')))
        return actions_rules


class Calbamol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=6) -> None:
        super().__init__('calbamol', activation_rules, 48, 6)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                    destination='temperatura',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                    destination='temperatura',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                    destination='temperatura',
                    then=('decrease','medium')))
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                    destination='temperatura',
                    then=('decrease','high')))

            if env.get_parameter('plaqueta') != None and env.get_parameter('plaqueta').value<=10:
                
                actions_rules.append(Rule(
                    {'plaqueta':'media'},
                    destination='plaqueta',
                    then=('increase','low')))
                actions_rules.append(Rule(
                    {'plaqueta':'baja'},
                    destination='plaqueta',
                    then=('increase','medium')))
                actions_rules.append(Rule(
                    {'plaqueta':'alta'},
                    destination='plaqueta',
                    then=('increse','low')))
        return actions_rules

class Jarabe(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=8) -> None:
        super().__init__('jarabe', activation_rules, 48, 8)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>=15:
                actions_rules.append(Rule(
                    {'tos':'baja'},
                    destination='tos',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'tos':'media'},
                    destination='tos',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'tos':'alta'},
                    destination='tos',
                    then=('decrease','medium')))
        return actions_rules

class Antibiotico(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=12) -> None:
        super().__init__('antibiotico', activation_rules, 48, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                    destination='temperatura',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                    destination='temperatura',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                    destination='temperatura',
                    then=('decrease','medium')))
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                    destination='temperatura',
                    then=('decrease','high')))

            if env.get_parameter('tos') != None and env.get_parameter('tos').value>=22:
                actions_rules.append(Rule(
                    {'tos':'baja'},
                    destination='tos',
                    then=('decrease','low')))
                actions_rules.append(Rule(
                    {'tos':'media'},
                    destination='tos',
                    then=('decrease','medium')))
                actions_rules.append(Rule(
                    {'tos':'alta'},
                    destination='tos',
                    then=('decrease','medium')))
        return actions_rules


class Plaquetol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=6) -> None:
        super().__init__('plaquetol', activation_rules, 24, 6)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            actions_rules.append(Rule(
                {'plaqueta':'media'},
                destination='plaqueta',
                then=('increase','low')))
            actions_rules.append(Rule(
                {'plaqueta':'baja'},
                destination='plaqueta',
                then=('increase','medium')))
            actions_rules.append(Rule(
                {'plaqueta':'alta'},
                destination='plaqueta',
                then=('decrese','low')))
        return actions_rules