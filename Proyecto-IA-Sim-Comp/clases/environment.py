from parameters import Parameter
class Environment:
    def __init__(self,parameters_list):
        self._env_parameters_list=parameters_list
        
    @property
    def final_state(self):
        final=True
        for params in self.env_parameters_list:
            final &=params.in_limits
        return final