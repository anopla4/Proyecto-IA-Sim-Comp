from typing import Callable, Dict

class Variable:
    def Variable(self, name:str, value:float,
        ranges:Dict[str,tuple[float,float]], membresy_functions:Dict[str, Callable[[float], float]]):
        self.name = name
        self.value = value
        self.ranges = ranges
        self.membresy_functions = membresy_functions

    def aply_memebresy_funtions(self, target:str, value:float)->float:
        """
        Devuelve el grado de pertenencia del valor especificado 
        a un deteminado elemento del conjunto difuso.
        """
        return self.membresy_functions[target](value)

    def get_defuzzy_values(self)->Dict[str,float]:
        """
        Devuelve los valores de pertencia de la variable en base a su valor actual
        """
        return { k:v(self.value) for k,v in self.membresy_functions }


