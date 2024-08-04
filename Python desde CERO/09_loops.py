### loops / Bucles ###

'''En programación también hacemos muchas tareas repetitivas.
Para manejar tareas repetitivas, los lenguajes de programación utilizan bucles.
El lenguaje de programación Python también proporciona los siguientes tipos de dos bucles:'''

# while loop
# for loop 


 
'''Usamos la palabra reservada while para hacer un bucle while.
 Se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una
 condición determinada. Cuando la condición se vuelve falsa, las líneas de código después del
 bucle continuarán ejecutándose.'''

# while condicion:
#     el codigo va acá

# While se pasa una condición ( While , True [Mientras sea verdadero haz algo])

my_condition = 0

while my_condition < 10:
    print(my_condition) 
    # my_condition = my_condition + 2
    my_condition += 2 # es la misma forma
else:  # Es opcional 
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa") # Aparece una vez cumplido la condicion

while my_condition < 20:  # Se repite hasta cumplir su condición
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break # Detiene la ejecución

    print(my_condition)

#El while repite varias veces en funcion de una CONDICIÓN
#El for se repite tantas veces como elementos tengamos iterables

# For  nos sirve para iterar un listado de elemento

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:  # se ejecuta tantas veces como elementos tenga
    print(element)       # y accedera a uno de los ele,entos del listado
    # 35
    # 24
    # 62
    # 52
    # 30
    # 30
    # 17

my_tuple = (26, 1.71, "Matias", "Benavides", "AlilaAstrea")

for element in my_tuple:  # se ejecuta tantas veces como elementos tenga
    print(element) 
    # 26
    # 1.71
    # Matias
    # Benavides
    # AlilaAstrea

my_set = {"Matiti", "Beniti", 266}
    
for element in my_set:  # se ejecuta tantas veces como elementos tenga
    print(element) 
    # 266
    # Matiti
    # Beniti

my_dict = {"Nombre":"Matias", "Apellido": "Benavides", "Edad": 26, 1: "Python"}

for element in my_dict:  # se ejecuta tantas veces como elementos tenga
    print(element)   # con my_dict.values() imprime los valores
    # Nombre
    # Apellido
    # Edad
    # 1


for element in my_dict.values():
    print(element)
    if element == 26:
        break # Se para hasta 26, y la clave "Python" de 1 no se muestra
    print("Se ejecuta") 
    # Matias
    # Se ejecuta
    # Benavides
    # Se ejecuta
    # 26          # cumple el ciclo hasta que rompemos el bucle   

else:  # este else pertenece a for, no al if element
    print("El bucle for para diccionario ha finalizado")

# Con break podemos detener el bucle for al igual que con un while

print("La ejecucición continua y segundo ejemplo con continue")

for element in my_dict.values():
    print(element)
    if element == 26:
        continue # en vez de romper el bucle con break, con continue sigue
    print("Se ejecuta volviendo al for ademas agrega Python")
else:  
    print("El bucle for para diccionario ha finalizado")


# ---------------------------------------------------------------------------------------------

# Break: Usamos break cuando queremos salir o detener el ciclo.
#  syntax
# while condition: 
#     code goes here
#     if another_condition:
#         break

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break   # Sigue el loop con 0,1,2 y cuando llega el 3 se detiene


# Continuar: Con la instrucción continuar podemos omitir la iteración actual y
#  continuar con la siguiente:
#    syntax 
# while condition:
#     code goes here
#     if another_condition:
#         continue

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

#For#

'''Una palabra clave for se utiliza para crear un bucle for, similar a otros lenguajes de
programación, pero con algunas diferencias de sintaxis. El bucle se utiliza para iterar sobre
una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).'''

#  syntax
# for iterator in lst:
#     code goes here

numeros = [0, 1, 2, 3, 4, 5]

# número es un nombre temporal para hacer referencia a los elementos de la lista,
#  válido solo dentro de este bucle
for numero in numeros: 
    print(numero)       # the numbers will be printed line by line, from 0 to 5


# For loops en un string

#  syntax
# for iterator in string:
#     code goes here

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


# For loop en una tupla

#  syntax
# for iterator in tpl:
#     code goes here

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# Bucle for con diccionario Al recorrer un diccionario se obtiene la clave del mismo.

#    syntax
# for iterator in dct:
#     code goes here

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items(): # el metodo items() devuelve keys y values
    print(key, value) # De esta manera obtenemos tanto las claves como los valores impresos.


# For en un set {conjuntos}

#  syntax
# for iterator in st:
#     code goes here

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# Recordatorio de break y continue ejemplos

#  syntax
# for iterator in sequence:
#     code goes here
#     if condition:
#         break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break # Se detiene al llegar al 3


# Continuar: utilizamos continuar cuando queremos omitir
# algunos de los pasos en la iteración del bucle.

#    syntax
# for iterator in sequence:
#     code goes here
#     if condition:
#         continue.

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")  
# para condiciones abreviadas se necesitan declaraciones if y else imprimir('fuera del bucle')
print('outside the loop')


# En el ejemplo anterior, si el número es igual a 3, el paso después de la condición
#  (pero dentro del bucle) se omite y la ejecución del bucle continúa si quedan iteraciones.


# Funcion range() explicado


# La función range() se utiliza como lista de números.
#  El rango (start, end, step) toma tres parámetros: inicio, fin e incremento.
#  De forma predeterminada, comienza desde 0 y el incremento es 1.
#  La secuencia de rango necesita al menos 1 argumento (end).
#  Creando secuencias usando rango

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# syntax
# for iterator in range(start, end, step):

for number in range(11):
    print(number)   # prints 0 to 10, not including 11



# Bucles anidados
# Se pueden hacer bucles dentro de bucles 

#  syntax
# for x in y:
#     for t in x:
#         print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill) # Imprime los valores de skills


# Si queremos ejecutar algún mensaje cuando finalice el bucle, usamos else.

#  syntax
# for iterator in range(start, end, step):
#     do something
# else:
#     print('The loop ended')

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

#Pass

# En Python, cuando se requiere una declaración (después del punto y coma),
#  pero no nos gusta ejecutar ningún código allí,
#  podemos escribir la palabra pasar para evitar errores.
#  También podemos usarlo como marcador de posición para declaraciones futuras.

for number in range(6):
    pass


### Ejercicios -----------------------------------------------------------------------------#

# Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while.

for numerito in range(0,11):
    print(numerito, "El ciclo for")

count = 0
while count < 11:
    print(count , "El numero ahora es ")
    count = count + 1
    if count == 11:
        
        break

# Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.

valores = [10,9,8,7,6,5,4,3,2,1,0]

for numerete in range(len(valores) -1, -1, -1) :
    print(valores[numerete], "whyu")
    

for item in reversed(valores):
    print(item)



# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end")  
# # para condiciones abreviadas se necesitan declaraciones if y else imprimir('fuera del bucle')
# print('outside the loop')