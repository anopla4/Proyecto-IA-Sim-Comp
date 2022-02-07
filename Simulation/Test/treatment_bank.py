from Simulation.environment import Environment
from random import random


def dipirona_simple_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.7:
        if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
            env.update_parameter('dolor de cabeza', -4.4)
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
            env.update_parameter('fiebre', -1)
    return env

def dipirona_doble_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.82:
        if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
            env.update_parameter('dolor de cabeza', -6.8)
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
            env.update_parameter('fiebre', -1.5)
    return env

def calbamol_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.40:
        if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
            env.update_parameter('dolor de cabeza', -2)
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
            env.update_parameter('fiebre', -0.5)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', 3)
    elif r < 0.80:
        if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
            env.update_parameter('dolor de cabeza', -3)
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
            env.update_parameter('fiebre', -0.5)
    return env

def jarabe_action(time: int, env: Environment) -> Environment:
    r = random()
    if r < 0.75:
        if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
            env.update_parameter('tos', -6)
    return env


def antibiotico_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.5:
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>38:
            env.update_parameter('fiebre', -1.6)
        if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
            env.update_parameter('tos', -10)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', 2.4)
    if r < 0.8:
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>38:
            env.update_parameter('fiebre', -1.4)
        if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
            env.update_parameter('tos', -6)
    else:
        if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>38:
            env.update_parameter('fiebre', -1.0)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', 6)
    return env

def plaquetol_action(time: int, env: Environment) -> Environment:
    r = random()
    if r < 0.5:
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', 2)
    if r < 0.8:
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', 5)
    return env