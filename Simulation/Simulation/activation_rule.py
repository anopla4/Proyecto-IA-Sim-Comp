from typing import Dict, Tuple
from .environment import Environment

class ActivationRule:
    def __init__(self, 
        parameters_conditions:Dict[str,Tuple[float,float]], time_condition:Tuple[float,float]):
        self._parameters_conditions = parameters_conditions
        #self._then = then
        self._time_conditions = time_condition

    #def get_target(self)-> str:
    #    return self._then

    def check_time(self, enviroment_time:int)->bool:
        '''
        Returns True if time condition are met.
        '''
        return self._time_conditions[0] <= enviroment_time <= self._time_conditions[1]

    def check_envioroment_condition(self, env:Environment)->bool:
        """ Returns True if all rule conditions are met in the environment"""
        for param_name, condition in self._parameters_conditions.items():
            param = env.get_parameter(param_name)
            if param == None or not (condition[0] <= param.value <= condition[1]):
                return False
        return True