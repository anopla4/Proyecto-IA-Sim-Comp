from .fuzzy_functions import *
import matplotlib.pyplot as plt
import numpy as np

"""
A continuacion se presentan 3 funciones triangulares que reprentan los
3 conjuntos difusos de una variable arbitraria, cada una de estas funciones
se instanciaron con parametros distintos y se les aplico el metodos de mandami
con valores de corte distintos. Este ejemplo de prueba esta basado en 
el sistem difuso visto en Conferencia
"""

#Primera funcion
trian1=triang_shape([5,10,15])
f1=inference_by_mandami(0.15,trian1)

#Segunda funcion
trian2=triang_shape([10,15,20])
f2=inference_by_mandami(0.7, trian2)

#Tercera funcion
trian3=triang_shape([15,20,25])
f3=inference_by_mandami(0.8, trian3)

# Lista con todas las funciones  
func_list=[f1,f2,f3]

""" 
funcion que se obtiene luego de aplicar el metodo de agregacion  por maximo
a las 3 funciones que previamente se les aplico mandami
"""
current_func=max_agreg(func_list)

x=np.linspace(5, 25)
for i in x:
    plt.scatter(i,current_func(i))
plt.show()
print(defuzzing_by_centroid(current_func, 5, 25))
