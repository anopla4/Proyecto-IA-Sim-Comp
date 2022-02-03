from Simulation.agent import Agent
from Simulation.environment import Environment
from random import random

class DipironaSimple(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=8) -> None:
        super().__init__('dipirona 1', activation_rules, 24, 8)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.7:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                env.update_parameter('dolor de cabeza', -4.4)
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
                env.update_parameter('fiebre', -1)
        return env

class DipironaDoble(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('dipirona 2', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.82:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                env.update_parameter('dolor de cabeza', -6.8)
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>=37:
                env.update_parameter('fiebre', -1.5)
        return env

class Calbamol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=6) -> None:
        super().__init__('calbamol', activation_rules, 48, 6)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
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

class Jarabe(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=12) -> None:
        super().__init__('jarabe', activation_rules, 48, 12)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.75:
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                env.update_parameter('tos', -6)
        return env

class Antibiotico(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=12) -> None:
        super().__init__('antibiotico', activation_rules, 36, 12)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.5:
            if env.get_parameter('fiebre') != None and env.get_parameter('fiebre').value>38:
                env.update_parameter('fiebre', -1.6)
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                env.update_parameter('tos', -10)
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

class Plaquetol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('plaquetol', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> Environment:
        self._current_action_time+=self._repetition
        r = random()
        if r < 0.5:
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', 2)
        if r < 0.8:
            if env.get_parameter('plaqueta') != None:
                env.update_parameter('plaqueta', 4)
        return env