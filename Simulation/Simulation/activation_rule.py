from typing import Dict, Tuple
from .environment import Environment

class ActivationRule:
    def __init__(self, 
        parameters_conditions:Dict[str,Tuple[float,float]], time_condition:Tuple[float,float], 
        agents_conditions:Dict[str, list[str]] = {}):
        self._parameters_conditions = parameters_conditions
        self._agents_conditions = agents_conditions
        self._time_conditions = time_condition

    def check_time(self, enviroment_time:int)->bool:
        """ Returns True if time conditions are met in the current time"""
        return self._time_conditions[0] <= enviroment_time <= self._time_conditions[1]

    def check_envioroment_condition(self, env:Environment)->bool:
        """ Returns True if all rule conditions are met in the environment"""
        for param_name, condition in self._parameters_conditions.items():
            param = env.get_parameter(param_name)
            if param == None or not (condition[0] <= param.value <= condition[1]):
                return False
        return True

    def check_agents_conditions(self, active_agents:list[str])->bool:
        """ Returns True if all agents conditions are met in the active agents"""
        for agent_name in self._agents_conditions['active']:
            if not agent_name  in active_agents:
                return False
        for agent_name in self._agents_conditions['inactive']:
            if agent_name in active_agents:
                return False
        return True

    def check_all(self, environment_time:int, env:Environment, active_agents:list[str])->bool:
        """ Returns True if time conditions are met """
        return self.check_time(environment_time) and self.check_envioroment_condition(env) and self.check_agents_conditions(active_agents)