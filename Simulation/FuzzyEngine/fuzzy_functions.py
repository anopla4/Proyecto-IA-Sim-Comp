
from scipy import integrate
from math import exp

def inference_by_mandami(param,func):
    """
    funcion para obtener la inferencia usando el método de Mandami
    param es el valor de corte y func es la función a la que se le hará el
    el corte. Devuelve una función que es el resultado de aplicar el método de
    Mandami en parámetro
    """
    def inner(*args):
        return min(param,func(*args))
    return inner

# funcion para agrupar las salidas del fuzzy -> metodo Max
def max_agreg(list_functions):
    """
    Recibe una lista de funciones, y se devuelve una funcion que recibe que
    un parametro y devuelve el mayor de todos los f(x) para todas las funciones
    en la lista para un mismo x. Se espera que todas las funciones hayan 
    sido previamente obtenidas por el metodo de Mandami
    """
    def inner(*args):
        max_val=0
        for i in list_functions:
            max_val=max(max_val,i(*args))
        return max_val
    return inner

def discret_centroid(func,lower_range,upper_range,step=1):
    """
    Funcion hecha para defuzzificar un valor aplicando el metodo de los 
    centroides en una variable con dominio discreto
    """
    num=0
    den=0
    for i in range(lower_range,upper_range,step):
        num+=i*func(i)
        den+=func(i)
    return num/den


def defuzzing_by_centroid(agregation_function,lower_range:float,upper_range:float):
    """
    Funcion hecha para defuzzificar un valor aplicando el metodo de los 
    centroides en una variable con dominio continuo
    """
    func= lambda f: lambda x: x*f(x)
    num=integrate.quad(func(agregation_function),lower_range,upper_range)
    den=integrate.quad(agregation_function,lower_range,upper_range)
    return num[0]/den[0]

# funciones fuzzy basicas:

def singleton(x0):
    """
    Funcion singleton, recibe un parametro y devuelve una instancia de la
    funcion singleton con el valor fijado a x0
    """
    def inner(x):
        if x==x0:
            return 1.0
    
        else :
            return 0
    return inner

def triang_shape(params):
    """
    Funcion triangular , recibe como parametro una lista [a,b,c] con todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
    """
    a=params[0]
    b=params[1]
    c=params[2]
    assert a<=b<=c
    def inner(x):
        result=0
        if x<=a or x>=0:
            result=0
        if a<x<=b:
            result=(x-a)/(b-a)
    
        if b<x<c:
            result=(c-x)/(c-b)
        return result
    
    return inner
            
def sigmoidal_shape(params):
    """
    Funcion S, recibe como parametro una lista [a,b,c] con todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
    """
    a=params[0]
    b=params[1]
    def inner(x):
        return 1/(1+exp(-a*(x - b)))
    return inner

def trapezoidal_shape(params):
    """
    Funcion trapezoidal , recibe como parametro una lista [a,b,c,d] con todos
    valores reales que representan las distintas regiones de la funcion.
    Devuelve una funcion instanciada para un conjunto de parametros 
    especificos
    """
    a=params[0]
    b=params[1]
    c=params[2]
    d=params[3]
    assert a<=b<=c<=d
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