from abc import ABC, abstractmethod
from .environment import Environment
from .activation_rule import ActivationRule

class Agent(ABC):
    def __init__(self, name:str, activation_rules:list[ActivationRule], 
        efect_time:int, repetition:int) -> None:
        self._name = name
        self._active:bool = False
        self._ag_history = None
        self._activation_rules:list[ActivationRule] = activation_rules
        self._current_action_time = 0   # increse rep by rep if take action
        self._efect_time = self.__calculate_efect_time(efect_time, repetition)
        self._repetition = repetition
        self._action = None #function

    def __calculate_efect_time(self, efect_time, repetition):
        times = efect_time//repetition
        return times*repetition

    @property
    def inner_action(self):
        return self._action

    @inner_action.setter
    def inner_action(self, action):
        self._action = action

    def action(self, time:int, env:Environment) -> Environment:
        self._current_action_time+=self._repetition
        return self._action(time,env)

    def check_activation_conditions(self, time:int, env:Environment)-> bool:
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
        '''
        Returns the repetition time of the agent action
        '''
        return self._repetition

    @property
    def name(self)->str:
        '''
        Returns the name of the agent
        '''
        return self._name