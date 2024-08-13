### Modules ###

# El concepto de modulo entra en el caso de si queremos trabajar con archivos de otras rutas

'''
Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones que se pueden incluir en una aplicación. Un módulo podría ser un archivo que contenga una sola variable, una función o una gran base de código.
'''
# un modulo no solo se queda en utilizar otros archivos dentro de nuestro programa, si no tambien librerias del sistema, liberia de otras personas, (descargadas de github por ej)


# from 10_functions import sum_two_values  La nomenclatura no es valida para los modulos así que se tendrá que renombrar

import mymodule
mymodule.sumValues(5, 3, 1) # 9

mymodule.printValue("Hola Python!") # Hola Python!


from mymodule import printValue, sumValues

sumValues(5, 3, 1)
printValue("Hola Python") # Hola Python


# Tenemos modulos creados por el sistema

import math

print(math.pi) # 3.141592653589793
print(math.pow(2, 8)) # dos elevado 8 o 2**8 256.0

print(2**8) # 256

from math import pi

print(pi) # 3.141592653589793

from math import pi as PI_VALUE

print(PI_VALUE) # 3.141592653589793