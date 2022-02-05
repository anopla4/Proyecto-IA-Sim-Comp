from typing import Dict

class Rule:
    def __init__(self, parameters_conditions:Dict[str,str], param_destination:str, then:tuple[str,str]):
        self._parameters_conditions = parameters_conditions
        self._destination = param_destination
        self.then = then

    @property
    def target(self)-> str:
        return self.then[0]

    @property
    def destination(self)->str:
        return self._destination

    @property
    def conditions(self)->Dict[str,str]:
        return self._parameters_conditions