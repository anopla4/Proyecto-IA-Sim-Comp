from .membresy_function import MembresyFunction

class Singleton(MembresyFunction):
    """
    Singleton function, receives a parameter and with the property function
    returns an instance of the singleton function with the value set to x0
    """
    def __init__(self,x0:float):
        self._x0=x0
    
    @property
    def function(self):
        x0=self._x0
        def inner(x):
            if x==x0:
                return 1
            else :
                return 0
        return inner
    
    @property
    def limits(self):
        return (self._x0,self._x0)