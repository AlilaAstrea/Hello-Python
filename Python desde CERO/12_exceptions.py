### Exceptions Handling ###
# Manejo de errores

# Python es de tipado dinamico por : donde un tipo inicialmente es un str lo podemos pasar a int
# Por lo tanto no es de tipado fuerte

# print(5 + "5")


numberOne, numberTwo = 5, 1

numberTwo = "1"

if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplió")  # manejamos un error pero lo adecuado es try except


# Try except

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")


# Try except else finally

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecución continúa correctamente")
finally: # Opcional
    print("La ejecución continúa")


# Excepciones por tipo

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except TypeError: # Esto se ejecuta SOLO si ocurre un TypeError
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Captura de la información de la excepción

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError as error: # error es una variable no un nombre reserv.
    print(error)
    # capturamosq ue fue lo que provocó el error
except Exception as my_random_error_name:
    print(my_random_error_name)
