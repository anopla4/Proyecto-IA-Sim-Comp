from typing import Dict, Tuple
from .environment import Environment
from .parameter import Parameter

class ActivationRule:
    def __init__(self, 
        parameters_conditions:Dict[Parameter,Tuple[float,float]], time_condition:Tuple[float,float]):
        self._parameters_conditions = parameters_conditions
        self._time_conditions = time_condition

    def check_time(self, enviroment_time:int)->bool:
        '''
        Returns True if time condition are met.
        '''
        return self._time_conditions[0] <= enviroment_time <= self._time_conditions[1]

    def check_envioroment_condition(self, env:Environment)->bool:
        """ Returns True if all rule conditions are met in the environment"""
        for param, condition in self._parameters_conditions.items():
            param_ = env.get_parameter(param.name)
            if param_ == None or not (condition[0] <= param_.value <= condition[1]):
                return False
        return True