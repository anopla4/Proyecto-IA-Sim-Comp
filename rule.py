from typing import Dict
from env import Env

class Rule:
    def Rule(self, 
        parameters_conditions:Dict, time_condition, then:str):
        self._parameters_conditions = parameters_conditions
        self._then = then
        self._time_conditions = time_condition

    def get_target(self)-> str:
        return self._then

    def check_time(self, enviroment_time:int)->bool:
        return enviroment_time >= self._time_conditions

    def check_envioroment_condition(self, env:Env)->bool:
        """ Returns True if all rule conditions are met in the environment"""
        pass