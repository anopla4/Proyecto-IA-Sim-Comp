from typing import Dict
from .parameter import Parameter

class Environment:
    def __init__(self,parameters:list[Parameter]):
        self._parameters:list[Parameter]=parameters
        
    def get_parameter(self, param_name:str)->Parameter:
        '''
        Returns the instance of the named parameter "name". 
        If not found, returns None
        '''
        for p in self._parameters:
            if p.name == param_name:
                return p
        return None

    @property
    def parameters(self)->list[Parameter]:
        '''
        Returns a list with the parameters of the environment
        '''
        return self._parameters

    def update_parameter(self, param_name, value:float)->None:
        '''
        Adds the value specified in "value" to the parameter 
        specified in "param_name" if this parameter exists in 
        the environment
        '''
        for p in self._parameters:
            if p.name == param_name:
                p.value+=value
                return
        return
    
    def final_state(self):
        '''
        Returns true if at least one parameter of the environment is outside 
        the extreme limits of life (bad_limits).
        '''
        for param in self._parameters:
            if not param.in_limits:
                return True
        return False

    def copy(self):
        '''
        Returns a exact copy of environment
        '''
        param_list = []
        for p in self._parameters:
            param_list.append(Parameter(p.name, p.value, p.low_good_limit, p.upp_good_limit, p.low_bad_limit, p.upp_bad_limit))
        return Environment(param_list)

    def get_params_dict(self)->Dict[str,float]:
        '''
        Returns a dictionary with the parameters, 
        where the key is the name and the value is the value of the parameter
        '''
        params_dict = {}
        for param in self._parameters:
            params_dict[param.name]= param.value
        return params_dict

    def __str__(self) -> str:
        representation = ""
        for p in self._parameters:
            representation+=str(p)+"\n"
        return representation