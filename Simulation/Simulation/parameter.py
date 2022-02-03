class Parameter:
    def __init__(self,name:str,value:float,
    low_good_limit:float, upp_good_limit:float, low_bad_limit:float,upp_bad_limit:float):
        self._name=name
        self._value=value
        self._low_good_limit=low_good_limit
        self._upp_good_limit=upp_good_limit
        self._low_bad_limit=low_bad_limit
        self._upp_bad_limit=upp_bad_limit
    
    @property
    def in_good_limits(self):
        return self._low_good_limit<=self._value<=self._upp_good_limit

    @property
    def in_limits(self):
        return self._low_bad_limit<=self._value<=self._upp_bad_limit
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,new_value:float):
        self._value=new_value
    
    @property
    def low_bad_limit(self):
        return self._low_bad_limit
    
    @property
    def upp_bad_limit(self):
        return self._upp_bad_limit

    @property
    def low_good_limit(self):
        return self._low_good_limit
    
    @property
    def upp_good_limit(self):
        return self._upp_good_limit
    
    def __str__(self) -> str:
        return f"""{self.name}:{self.value}"""