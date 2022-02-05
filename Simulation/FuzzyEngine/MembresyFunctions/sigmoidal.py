from .membresy_function import MembresyFunction
from math import exp

class Sigmoidal(MembresyFunction):
    """
    Sigmoidal function, receives as parameters a,b 
    with all real values that represent the different regions of the function.
    """
    def __init__(self,a:float,b:float):
        self._a=a
        self._b=b
    
    @property
    def function(self):
        a=self._a
        b=self._b
        def inner(x):
            return 1/(1+exp(-a*(x - b)))
        return inner
    
    @property
    def limits(self):
        return (self._x0,self._x0)