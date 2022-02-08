from FuzzyEngine.rule import Rule
from Simulation.environment import Environment
from random import random

def dipirona_action(time: int, env: Environment) -> list[Rule]:
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

def calbamol_action(time: int, env: Environment) -> list[Rule]:
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
                then=('decrease','high')))
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

def jarabe_action(time: int, env: Environment) -> list[Rule]:
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
                then=('decrease','high')))
            actions_rules.append(Rule(
                {'tos':'alta'},
                destination='tos',
                then=('decrease','high')))
    return actions_rules

def antibiotico_action(time: int, env: Environment) -> list[Rule]:
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
                then=('decrease','high')))
    return actions_rules

def plaquetol_action(time: int, env: Environment) -> list[Rule]:
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