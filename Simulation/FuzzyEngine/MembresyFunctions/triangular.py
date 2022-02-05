from abstract_function import membresy_function

class triangular(membresy_function):
    """
    Funcion triangular , recibe como parametros a,b y c  todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
    """
    def __init__(self,a:float,b:float,c:float):
        self._a=a
        self._b=b
        self._c=c
        assert a<=b<=c
    
    @property
    def function(self):
        a=self._a
        b=self._b
        c=self._c
        def inner(x):
            result=0
            if x<=a or x>=c:
                result=0
            if a<x<=b:
                result=(x-a)/(b-a)
            if b<x<c:
                result=(c-x)/(c-b)
            return result
        return inner
    
    @property
    def limits(self):
        return (self._a,self._c)
    
    