class Parameter:
    def __init__(self,name:str,value:float,inf_limit:float,upper_limit:float):
        self._param_name=name
        self._param_value=value
        self._param_inf_limit=inf_limit
        self._param_upper_limit=upper_limit
    
    @property
    def in_limits(self):
        return self._param_inf_limit<=self._param_value<=self._param_upper_limit
    
    @property
    def name(self):
        return self._param_name
    
    @property
    def value(self):
        return self._param_value
    
    @value.setter
    def value(self,new_value:float):
        self._param_value=new_value
    
    @property
    def inf_limit(self):
        return self._param_inf_limit
    
    @property
    def upper_limit(self):
        return self._param_upper_limit
    