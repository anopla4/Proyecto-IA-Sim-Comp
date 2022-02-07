from Simulation.environment import Environment
from random import random

def tos_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.5:
        if env.get_parameter('tos') != None:
            env.update_parameter('tos', 0.4)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', -0.5)
    else:
        if env.get_parameter('tos') != None:
            env.update_parameter('tos', 0.4)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', -0.8)
    return env

def fiebre_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.4:
        if env.get_parameter('fiebre') != None:
            env.update_parameter('fiebre', 1)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', -1.5)
    elif r < 0.75:
        if env.get_parameter('fiebre') != None:
            env.update_parameter('fiebre', 1.4)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', -1.5)
    else:
        if env.get_parameter('fiebre') != None:
            env.update_parameter('fiebre', 1.8)
        if env.get_parameter('plaqueta') != None:
            env.update_parameter('plaqueta', -2.0)
        if env.get_parameter('dolor de cabeza') != None:
            env.update_parameter('dolor de cabeza', 3)
    return env


def dc_action(time:int, env:Environment)->Environment:
    r = random()
    if r < 0.75:
        if env.get_parameter('dolor de cabeza') != None:
            env.update_parameter('dolor de cabeza', 2.5)
    else:
        if env.get_parameter('dolor de cabeza') != None:
            env.update_parameter('dolor de cabeza', 4.5)
    return env
