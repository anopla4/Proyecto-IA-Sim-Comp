from typing import Dict, Tuple


class Rule:
    def Rule(self, parameters_conditions:list[tuple[str,str]], time_condition:Tuple[float,float],
        agents_conditions:Dict[str,list[str]],then:tuple[str,str]):
        self._parameters_conditions = parameters_conditions
        self.then = then

    def get_target(self)-> str:
        return self.then[0]