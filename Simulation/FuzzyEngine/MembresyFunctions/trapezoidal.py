from .membresy_function import MembresyFunction

class Trapezoidal(MembresyFunction):
    """
    Trapezoidal function, receives as parameters a, b, c and d with all
    real values that represent the different regions of the function.
    """

    def __init__(self,a:float,b:float,c:float,d:float):
        self._a=a
        self._b=b
        self._c=c
        self._d=d
        assert a<=b<=c<=d
    
    @property
    def function(self):
        a=self._a
        b=self._b
        c=self._c
        d=self._d
        def inner(x):
            result=0.0
            if x<=a or x>=d:
                result=0.0      
            if a<x<=b:
                result=(x-a)/(b-a)
            if b<x<c:
                result=1.0
            if c<x<d:
                result=(d-x)/(d-c)
            return result
        
        return inner
        
    @property    
    def get_limits(self):
        return (self._a,self._d)