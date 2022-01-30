from abc import ABC, abstractmethod
from env import Env
from rule import Rule

class Agent(ABC):
    def __init__(self, name:str, probability_function, activation_rules, efect_time, repetition) -> None:
        self._name = name
        self._active:bool = False
        self._ag_history = None
        self._activation_rules:list[Rule] = activation_rules
        self._current_action_time = 0   # increse rep by rep if take action
        self._efect_time = efect_time
        self._repetition = repetition
        self._probability_function = probability_function

    @abstractmethod
    def action(self, time:int, env:Env) -> Env:
        pass

    def check_activation_conditions(self, time:int, env:Env)-> bool:
        """ Returns True if the activation conditions are met."""
        for rule in self._activation_rules:
            if rule.check_time(time) and rule.check_envioroment_condition(env):
                return True
        return False
    
    def finish_action(self)->bool:
        """
        True if action time == efect time. Restart action time
        """
        finish = self._current_action_time == self._efect_time
        if finish:
            self._current_action_time = 0
        return finish

    @property
    def repetition(self)->int:
        return self._repetition

    @property
    def name(self)->str:
        return self._name