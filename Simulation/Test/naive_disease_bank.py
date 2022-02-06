from Simulation.agent import Agent
from Simulation.environment import Environment
from FuzzyEngine.rule import Rule
from random import random

class Tos(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=8) -> None:
        super().__init__('tos', activation_rules, 48, 8)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            actions_rules.append(Rule(
                {'plaqueta':'baja'},
                destination='plaqueta',
                then=('decrease','medium')))
            actions_rules.append(Rule(
                {'plaqueta':'media'},
                destination='plaqueta',
                then=('decrease','medium')))
            actions_rules.append(Rule(
                {'plaqueta':'alta'},
                destination='plaqueta',
                then=('decrease','medium')))
            actions_rules.append(Rule(
                {'tos':'baja'},
                destination='tos',
                then=('increase','medium')))
            actions_rules.append(Rule(
                {'tos':'media'},
                destination='tos',
                then=('increase','medium')))
            actions_rules.append(Rule(
                {'tos':'alta'},
                destination='tos',
                then=('increase','medium')))
        return actions_rules

class Fiebre(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=12) -> None:
        super().__init__('fiebre', activation_rules, 48, 8)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 1:
            actions_rules.append(Rule(
                {'temperatura':'baja'},
                destination='temperatura',
                then=('increase','medium')))
            actions_rules.append(Rule(
                {'temperatura':'media'},
                destination='temperatura',
                then=('increase','high')))
            actions_rules.append(Rule(
                {'temperatura':'alta'},
                destination='temperatura',
                then=('increase','medium')))
            actions_rules.append(Rule(
                {'temperatura':'muy alta'},
                destination='temperatura',
                then=('increase','low')))
            
            actions_rules.append(Rule(
                {'plaqueta':'baja'},
                destination='plaqueta',
                then=('decrease','low')))
            actions_rules.append(Rule(
                {'plaqueta':'media'},
                destination='plaqueta',
                then=('decrease','low')))
            actions_rules.append(Rule(
                {'plaqueta':'alta'},
                destination='plaqueta',
                then=('decrease','high')))

        return actions_rules