### Sets ### 

''''
https://www.youtube.com/watch?v=Kp4Mvapo5kc

4:32:54
'''
''' 
Un conjunto es una colección de elementos. Déjame llevarte de regreso a tu lección de Matemáticas de la escuela primaria o secundaria.
La definición matemática de un conjunto también se puede aplicar en Python. 
Set es una colección de elementos distintos desordenados y no indexados.
En Python, el conjunto se utiliza para almacenar elementos únicos y es posible encontrar la unión, 
intersección, diferencia, diferencia simétrica, subconjunto, superconjunto y conjunto disjunto entre conjuntos.
'''

my_set = set()
# utiliza la palabra reservada set

my_other_set = {}

print(type(my_set)) #<class 'set'>
print(type(my_other_set)) #<class 'dict'> Inicialmente es un diccionario

my_other_set = {"Matias","Benavides",35}
print(type(my_other_set)) #<class 'set'>

print(len(my_other_set)) # 3

my_other_set.add("AlilaAstrea")
print(my_other_set) # {'AlilaAstrea', 35, 'Benavides', 'Matias'}
# Un set no es una estructura ordenada 
# Un set no admite repetidos (imprimira en orden diferente)
# -------------------------------------------------------------------------- #

print("Matias" in my_other_set) # True
print("Matita" in my_other_set) # False

my_other_set.remove("Matias")
print(my_other_set) # {'Benavides', 35, 'AlilaAstrea'}

my_other_set.clear()  
# La ventaja es no aceptar repetidos y trabaja con estructuras que no sean ordenadas
print(len(my_other_set)) # 0

del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined


my_set = {"Matias","Benavides",35}
my_list = list(my_set)
print(my_list) # ['Matias', 35, 'Benavides']
print(my_list[0]) # Benavides

my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set) #{'Matias', 35, 'Benavides', 'Kotlin', 'Swift', 'Python'}
print(my_new_set.union(my_new_set)) # no duplica los datos, sale lo mismo.

print(my_new_set.union(my_new_set).union({"JavaScript", "C#"})) # {'C#', 'Matias', 35, 'Kotlin', 'Python', 'JavaScript', 'Swift', 'Benavides'}
# Esta vez si agrega elementos, por que son elementos que no teniamos antes

print(my_new_set.difference(my_set)) # {'Python', 'Kotlin', 'Swift'}
# Estamos buscando la diferencia de 'my_new_set' le estamos quitando los elementos de my_set
# osea my_new_set tiene:
#  {'C#', 'Matias', 35, 'Kotlin', 'Python', 'JavaScript', 'Swift', 'Benavides'}
# my_set tiene:
#  {"Matias","Benavides",35}
# Entonces quita matias, benavides, 35. No cuenta "JavaScript" y "C#" porque se hizo un
# union desde el print, osea solo para esa ejecución, no para ser guardado en el set

# --------------------------------------------------------------------------------------------- #


# (+) Ejemplos

# syntax Este método devuelve un nuevo conjunto.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3) # {'item3', 'item7', 'item5', 'item8', 'item4', 'item2', 'item6', 'item1'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# syntax Este método inserta un conjunto en un conjunto determinado.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# syntax Devuelve un conjunto de elementos que se encuentran en ambos conjuntos. ver el ejemplo
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}


# syntax Un conjunto puede ser un subconjunto o un superconjunto de otros conjuntos:
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
python.issuperset(dragon) 


# syntax Devuelve la diferencia entre dos conjuntos.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}


# syntax Entrega un conjunto con los elementos unicos de cada conjunto, omitiendo
# aquellos que se repitan en ambos
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


# syntax Si dos conjuntos no tienen uno o más elementos en común,
#  los llamamos conjuntos disjuntos.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


# Ejercicios ----------------------------------------------------------------------------------------#

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



# Encuentra la longitud del conjunto it_companies

print("La longitud de el conjunto it_companies es : ", len(it_companies))
# La longitud de el conjunto it_companies es :  7

# Añade 'Twitter' a it_companies

it_companies.add("Twitter")
print(it_companies)
# {'IBM', 'Microsoft', 'Oracle', 'Apple', 'Google', 'Twitter', 'Facebook', 'Amazon'}


# Inserte varias empresas de TI a la vez en el conjunto it_companies


otras_companias = {'AWS', 'Cisco Networking', 'Firefoxs', 'Brave'}
it_companies.update(otras_companias)
print(it_companies)
# {'Microsoft', 'Oracle', 'AWS', 'Brave', 'Cisco Networking', 'IBM', 'Twitter', 'Apple', 'Google', 'Firefoxs', 'Facebook', 'Amazon'} 



# Eliminar una de las empresas del conjunto it_companies
it_companies.pop()
print(it_companies)
# {'Cisco Networking', 'Apple', 'AWS', 'Google', 'IBM', 'Amazon', 'Twitter', 'Brave', 'Firefoxs', 'Microsoft', 'Oracle'}
# Elimino Facebook


# Cuál es la diferencia entre eliminar y descartar
# Se refiere a la diferencia entre remove() y discard()
# remove() : Elimina un elemento especifico del conjunto, pero si no se encuentra dará error
# discard(): Elimina un elemento y no genera error.

it_companies.remove('AWS')
print(it_companies)
# {'Brave', 'IBM', 'Twitter', 'Facebook', 'Cisco Networking', 'Oracle', 'Microsoft', 'Apple', 'Firefoxs', 'Amazon'}
it_companies.discard('pepe') # Aunque ponga AWS no me dara error y si pongo un elento que no existe tampoco
print(it_companies)


# Ejercicios Lvl 2 ----------------------------------------------------------------------------------------#

# Unir A y B
# se puede usar union() o update()

C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}

print(A.union(B)) # {19, 20, 22, 24, 25, 26, 27, 28}

A.union(B)
print(A) # Esta manera da {19, 20, 22, 24, 25, 26} faltando 27,28 , si se hace al revez osea B.union(A) dara bn

A.update(B)
print(A) # {19, 20, 22, 24, 25, 26, 27, 28}

# Encuentra una intersección B
# ( hace un conjunto (set) nuevo donde junta las coincidencias, en este ej numeros repetidos)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.intersection(B)) # {19, 20, 22, 24, 25, 26}  # 28 y 27 no estan en ambos


# es un subconjunto de b ( is A subset of B)

print(A.issubset(B)) # True esta es !!!!!
print(A.issuperset(B)) # False

print(B.issubset(A)) # False
print(B.issuperset(A)) # True



# ¿Son A y B conjuntos disjuntos? disjoint sets
# (Si no tienen datos iguales, seria False ya que si tiene iguales)

print(A.isdisjoint(B)) # False



# Unir A con B y B con A

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}

D = B.union(A)
print(D) # {19, 20, 22, 24, 25, 26, 27, 28}

#A.add(B) # add solo agrega solo elementos hashables (set es unhashable)


# ¿Cuál es la diferencia simétrica entre A y B?
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Entrega los elementos no repetidos de cada set , serian solo 28 y 27

print(A.symmetric_difference(B)) # {27, 28}


# Eliminar los conjuntos por completo

del A
del B
# print(A) NameError: name 'A' is not defined
# print(B) NameError: name 'B' is not defined


# Ejercicios lvl 3 ----------------------------------------------------------------------------------------#
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Convierte las edades a un conjunto y compara la longitud de la lista y el conjunto,
#  ¿cuál es mayor?

edad = set(age)
print(edad) # {19, 22, 24, 25, 26}

print(len(age)) # 8
print(len(edad)) # 5

if len(age) >= len(edad):
    print("la lista age es Mayor que edad")
else:
    print("el conjunto edad es Mayor que age")


# Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto

# una cadena es un string , un valor inmutable que almacena caracteres por ejemplo
cadena = "Esto es una cadena"

# Una lista es un cumulo de valores mutables que pueden ser utilizados como un diccionario
# Estos datos pueden se pueden unir entre otras listas y tambien cambiar su valor
lista = []
lista = list()

# Una Tupla es una coleccion de valores inmutables los cuales no pueden ser modificables
# Tambien entregan los datos de manera ordenada, de la misma forma que se encuentran agregados
tupla = tuple()
tupla = ()

#Un set o conjunto en español es una colección de valores inmutables, que no se pueden cambiar
# e irrepetibles que se obtienen de manera desordenada dentro de una petición
conjunto = set()
conjunto = {}

# Lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
print("Lista: " ,mi_lista) # Lista:  [1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
# Tupla
mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 8, 8)
print("Tupla: " ,mi_tupla) # Tupla:  (1, 2, 3, 4, 5, 6, 7, 8, 8, 8)

# Conjunto
mi_conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 8, 8}
print("Set: " ,mi_conjunto) # Set:  {1, 2, 3, 4, 5, 6, 7, 8}

# Diccionario
mi_diccionario = {"clave1": 1, "clave2": 2, "clave3": 3, "clave3": 3, "clave3": 4}
print("Diccionario: " ,mi_diccionario) # Diccionario:  {'clave1': 1, 'clave2': 2, 'clave3': 4}


# Soy profesora y me encanta inspirar y enseñar a la gente.
#  ¿Cuántas palabras únicas se han usado en la oración? Utilice los métodos de división y
#  configúrelo para obtener palabras únicas.

#Primero entrego la variable con la oracion en texto (str)
oracion = "Soy profesora y me encanta inspirar y enseñar a la gente"
#Uso la funcion split() para convertir el texto en una lista
x = oracion.split()
#Formateo la lista en un set() "conjunto"
formato = set(x)

# He imprimo la respuesta, como transforme la lista en un set, ahora puedo usar la función
# .difference() que me permite ver los valores unicos de un conjunto
# y como me pide cuantas palabras únicas hay en la oración utilizo la funcion len() para contar
print( "La cantidad de palabras unas son : ", len(formato.difference()))
print(formato.difference())
# {'y', 'profesora', 'Soy', 'me', 'enseñar', 'la', 'a', 'inspirar', 'encanta', 'gente'}  

# Ahora que lo veo, al convertirlo en set ya no hace falta usar difference si un set
# no permite repetidos.... Entonces seria mas simple como

# print(len(formato)) # 10
print(formato)
# {'encanta', 'me', 'inspirar', 'la', 'profesora', 'a', 'y', 'Soy', 'gente', 'enseñar'} 

