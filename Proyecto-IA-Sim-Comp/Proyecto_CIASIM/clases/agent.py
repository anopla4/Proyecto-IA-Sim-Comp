from environment import Environment
from abc import ABC,abstractmethod

class Agent(ABC):
    
    def init(self, name:str, probability_function, efect_time, repetition):
        self._name = name
        self._active:bool = False
        self._ag_history = None
        self._current_action_time = 0   # increse rep by rep if take action
        self._efect_time = efect_time
        self._repetition = repetition
        self._probability_function = probability_function

    @abstractmethod
    def action(self, time:int, env:Environment):
        pass
    
    def finish_action(self):
        """
        True if action time == efect time. Restart action time
        """
        finish = self._current_action_time == self._efect_time
        if finish:
            self._current_action_time = 0
        return finish

    @property
    def get_repetition(self):
        return self._repetition

    @property
    def name(self):
        return self._name
