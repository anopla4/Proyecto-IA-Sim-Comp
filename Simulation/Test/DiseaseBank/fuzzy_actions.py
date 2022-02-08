from FuzzyEngine.rule import Rule
from Simulation.environment import Environment
from random import random


def tos_action(time: int, env: Environment) -> list[Rule]:
    r = random()
    actions_rules = []
    if r < 1:
        actions_rules.append(Rule(
            {'plaqueta':'baja'},
            destination='plaqueta',
            then=('decrease','low')))
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

def fiebre_action(time: int, env: Environment) -> list[Rule]:
    r = random()
    actions_rules = []
    if r < 1:
        actions_rules.append(Rule(
            {'temperatura':'baja'},
            destination='temperatura',
            then=('increase','high')))
        actions_rules.append(Rule(
            {'temperatura':'media'},
            destination='temperatura',
            then=('increase','high')))
        actions_rules.append(Rule(
            {'temperatura':'alta'},
            destination='temperatura',
            then=('increase','low')))
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