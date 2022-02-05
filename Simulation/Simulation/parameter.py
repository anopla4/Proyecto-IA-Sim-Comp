from typing import Callable, Dict


class Parameter:
    def __init__(self,name:str,value:float,ranges:Dict[str,tuple[float,float]], 
    membresy_functions:Dict[str, Callable[[float], float]], low_good_limit:float, 
    upp_good_limit:float, low_bad_limit:float,upp_bad_limit:float):
        self._name=name
        self._value=value

        #fuzzy
        self.ranges = ranges
        self.membresy_functions = membresy_functions
        #---

        self._low_good_limit=low_good_limit
        self._upp_good_limit=upp_good_limit
        self._low_bad_limit=low_bad_limit
        self._upp_bad_limit=upp_bad_limit
    

    #fuzzy
    def aply_memebresy_funtions(self, target:str, value:float)->float:
        """
        Returns the membership degree of the specified value
        to a given element of the fuzzy set.
        """
        return self.membresy_functions[target](value)

    def get_defuzzy_values(self)->Dict[str,float]:
        """
        Returns the membership values of the variable based on its current value
        """
        return { k:v(self.value) for k,v in self.membresy_functions }

    #-----


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