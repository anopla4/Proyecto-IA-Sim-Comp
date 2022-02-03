from Simulation.agent import Agent
from Simulation.environment import Environment
from random import random

class Tos(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=3) -> None:
        super().__init__('tos', activation_rules, 72, 3)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
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

class Fiebre(Agent):
    def __init__(self, name: str, activation_rules, efect_time=72, repetition=4) -> None:
        super().__init__('fiebre', activation_rules, 72, 4)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
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

class DolorCabeza(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=4) -> None:
        super().__init__('dolor de cabeza', activation_rules, 36, 4)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.75:
            if env.get_parameter('dolor de cabeza') != None:
                env.update_parameter('dolor de cabeza', 2.5)
        else:
            if env.get_parameter('dolor de cabeza') != None:
                env.update_parameter('dolor de cabeza', 4.5)
        return env