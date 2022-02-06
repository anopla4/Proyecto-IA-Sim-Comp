from typing import Dict, Tuple, Callable

class MembresyFunction:
    @property
    def limits(self)->Tuple[float,float]:
        pass

    @property
    def function(self)->Callable[[float], float]:
        pass

class Parameter:
    def __init__(self,name:str,value:float, membresy_functions:Dict[str, MembresyFunction], 
    low_good_limit:float, upp_good_limit:float, low_bad_limit:float,upp_bad_limit:float):
        self._name=name
        self._value=value
        
        #fuzzy
        #self.ranges = ranges
        self._membresy_functions = membresy_functions
        self._left_limit, self._rigth_limit = self.__set_limits()
        #---
        
        self._low_good_limit=low_good_limit
        self._upp_good_limit=upp_good_limit
        self._low_bad_limit=low_bad_limit
        self._upp_bad_limit=upp_bad_limit
    
    def __set_limits(self):
        l_limit = 1e9
        r_limit = -1e9
        for _, mf in self._membresy_functions.items():
            limits = mf.limits
            if limits[0] < l_limit:
                l_limit = limits[0]
            if limits[1] > r_limit:
                r_limit = limits[1]
        return l_limit, r_limit

    #---------->        fuzzy     <------------------
    #
    def aply_memebresy_funtions(self, target:str, value:float)->float:
        """
        Returns the membership degree of the specified value
        to a given element of the fuzzy set.
        """
        return self._membresy_functions[target].function(value)

    def get_defuzzy_values(self)->Dict[str,float]:
        """
        Returns the membership values of the variable based on its current value
        """
        return { k:mf.function(self.value) for k,mf in self._membresy_functions.items() }
    
    @property
    def membresy_functions(self)->Dict[str, Callable[[float], float]]:
        dict_mf:Dict[str, Callable[[float], float]] = {}
        for var, mf in self._membresy_functions.items():
            dict_mf[var] = mf.function
        return dict_mf
    
    def get_definition_range(self)->Tuple[float,float]:
        '''
        Returns the range where membership functions are defined
        '''
        return self._left_limit, self._rigth_limit

    def get_extended_membresy_functions(self, extended)->Dict[str, Callable[[float], float]]:
        dict_mf:Dict[str, Callable[[float], float]] = {}
        for var, mf in self._membresy_functions.items():
            dict_mf[var] = mf.get_extended_function(extended)
        return dict_mf
    #
    #-----------------


    @property
    def in_good_limits(self):
        '''
        Returns True if the value of the parameter is within the limits 
        specified as good for it.
        '''
        return self._low_good_limit<=self._value<=self._upp_good_limit

    @property
    def in_limits(self):
        '''
        Returns True if the value of the parameter is within the extreme 
        limits specified for it.
        '''
        return self._low_bad_limit<=self._value<=self._upp_bad_limit
    
    @property
    def name(self):
        '''
        Returns the name of the parameter
        '''
        return self._name
    
    @property
    def value(self):
        '''
        Returns the value of the parameter
        '''
        return self._value
    
    @value.setter
    def value(self,new_value:float):
        self._value=new_value
    
    @property
    def low_bad_limit(self):
        '''
        Returns the lower bound of the parameter
        '''
        return self._low_bad_limit
    
    @property
    def upp_bad_limit(self):
        '''
        Returns the upper bound of the parameter
        '''
        return self._upp_bad_limit

    @property
    def low_good_limit(self):
        '''
        Returns the lower good bound of the parameter
        '''
        return self._low_good_limit
    
    @property
    def upp_good_limit(self):
        '''
        Returns the upper good bound of the parameter
        '''
        return self._upp_good_limit
    
    def __str__(self) -> str:
        return f"""{self.name}:{self.value}"""