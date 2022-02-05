from abstract_functions import membresy_function

class trapezoidal(membresy_function):
    
    """
    Funcion trapezoidal, recibe como parametros a,b,c y d con todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
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
            if x<=self._a or x>=self._d:
                result=0.0      
            if self._a<x<=self._b:
                result=(x-self._a)/(self._b-self._a)
            if self._b<x<self._c:
                result=1.0
            if self._c<x<self._d:
                result=(self._d-x)/(self._d-self._c)
            return result
        
        return inner
        
    @property    
    def get_limits(self):
        return (self._a,self._d)