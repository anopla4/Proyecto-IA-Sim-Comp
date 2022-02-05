from Simulation.agent import Agent
from Simulation.environment import Environment
from FuzzyEngine.rule import Rule
from random import random

class DipironaSimple(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=8) -> None:
        super().__init__('dipirona 1', activation_rules, 24, 8)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.7:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                param_destination='dolor de cabeza',
                then=('decrese',"little")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                then=('dolor de cabeza',"medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'bajo'},
                then=('dolor de cabeza',"bajo")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
        return actions_rules

class DipironaDoble(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('dipirona 2', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules= []
        if r < 0.50:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                then=('dolor de cabeza',"bajo")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                then=('dolor de cabeza',"medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'bajo'},
                then=('dolor de cabeza',"bajo")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
        # elif r < 0.85:
        #     if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
        #         actions_rules.append(Rule(
        #             {'temperatura':'muy alta'},
        #         then=('temperatura',"media")))
        #         actions_rules.append(Rule(
        #             {'temperatura':'alta'},
        #         then=('temperatura',"media")))
        return actions_rules

class Calbamol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=6) -> None:
        super().__init__('calbamol', activation_rules, 48, 6)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.40:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                then=('dolor de cabeza',"bajo")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                then=('dolor de cabeza',"medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'bajo'},
                then=('dolor de cabeza',"bajo")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                then=('temperatura','media')))
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy baja'},
                then=('plaqueta',"baja")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'baja'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy alta'},
                then=('plaqueta',"alta")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'alta'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'estable'},
                then=('plaqueta',"baja")))
        elif r < 0.80:
            if env.get_parameter('dolor de cabeza') != None and env.get_parameter('dolor de cabeza').value>5:
                actions_rules.append(Rule(
                    {'dolor de cabeza':'medio'},
                then=('dolor de cabeza',"bajo")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'alto'},
                then=('dolor de cabeza',"medio")))
                actions_rules.append(Rule(
                    {'dolor de cabeza':'bajo'},
                then=('dolor de cabeza',"bajo")))
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>=37:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                then=('temperatura','media')))
        return actions_rules

class Jarabe(Agent):
    def __init__(self, name: str, activation_rules, efect_time=48, repetition=12) -> None:
        super().__init__('jarabe', activation_rules, 48, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.75:
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
                    {'tos':'baja'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'media'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'alta'},
                then=('tos',"media")))
        return actions_rules

class Antibiotico(Agent):
    def __init__(self, name: str, activation_rules, efect_time=36, repetition=12) -> None:
        super().__init__('antibiotico', activation_rules, 36, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.5:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                then=('temperatura','media')))
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
                    {'tos':'baja'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'media'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'alta'},
                then=('tos',"media")))
        if r < 0.8:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                then=('temperatura','media')))
            if env.get_parameter('tos') != None and env.get_parameter('tos').value>5:
                actions_rules.append(Rule(
                    {'tos':'baja'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'media'},
                then=('tos',"baja")))
                actions_rules.append(Rule(
                    {'tos':'alta'},
                then=('tos',"media")))
        else:
            if env.get_parameter('temperatura') != None and env.get_parameter('temperatura').value>38:
                actions_rules.append(Rule(
                    {'temperatura':'muy alta'},
                then=('temperatura',"alta")))
                actions_rules.append(Rule(
                    {'temperatura':'alta'},
                then=('temperatura',"media")))
                actions_rules.append(Rule(
                    {'temperatura':'media'},
                then=('temperatura','baja')))
                actions_rules.append(Rule(
                    {'temperatura':'baja'},
                then=('temperatura','media')))
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy baja'},
                then=('plaqueta',"baja")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'baja'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy alta'},
                then=('plaqueta',"alta")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'alta'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'estable'},
                then=('plaqueta',"baja")))
        return actions_rules

class Plaquetol(Agent):
    def __init__(self, name: str, activation_rules, efect_time=24, repetition=12) -> None:
        super().__init__('plaquetol', activation_rules, 24, 12)

    def action(self, time: int, env: Environment) -> list[Rule]:
        self._current_action_time+=self._repetition
        r = random()
        actions_rules = []
        if r < 0.7:
            if env.get_parameter('plaqueta') != None:
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy baja'},
                then=('plaqueta',"baja")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'baja'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'muy alta'},
                then=('plaqueta',"alta")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'alta'},
                then=('plaqueta',"estable")))
                actions_rules.append(Rule(
                    {'plaqueta' : 'estable'},
                then=('plaqueta',"baja")))
        return actions_rules