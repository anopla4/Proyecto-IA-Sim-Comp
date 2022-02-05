from abstract_function import membresy_function
from math import exp
class sigmoidal(membresy_function):
    """
    Funcion sigmoidal, recibe como parametros a,b con todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
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