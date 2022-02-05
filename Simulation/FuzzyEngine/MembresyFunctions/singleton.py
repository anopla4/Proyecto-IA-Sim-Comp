from abstract_function import membresy_function

class singleton(membresy_function):
    """
    Funcion singleton, recibe un parametro y devuelve una instancia de la
    funcion singleton con el valor fijado a x0
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