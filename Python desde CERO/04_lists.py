### Lists ###

# Quitar Para ejecutar los ejemplos 

empy_list = list() # esto es una lista vacia, no un item en la lista
print(len(empy_list))

my_list = list()
my_other_list = [] # tambien es una lista
print(len(my_list)) # 0 (longitud)

# Una lista al final no deja de ser una caja en el que vamos añadiendo elementos cada uno en una posicion ( 1° elemento = posicion 0, 2° elemento = posicion 1)


#array de elementos

my_list = [26, 24, 62, 52, 30, 30, 17]

print(len(my_list)) # 7  # forma de agrupar datos

my_other_list = [26, 1.70, "Matias", "Benavides"]
print(type(my_other_list)) # <class 'list'>

# Un array es un tipo de lista. Una lista es un tipo de datos abstractos que implica una secuencia ordenada de valores

print(my_other_list[0]) # 26
print(my_other_list[1]) # 1,70
print(my_other_list[-1]) # Benavides

# para contar elementos de la propia lista utilizamos el count
print(my_other_list.count("Matias")) # 1 
print(my_list.count(30)) # 2

age, height, name, surname = my_other_list
print(name) # Matias

# age, height, name = my_other_list
# print(name) # Matias        # da error por falta de un elemento de la propia lista

# Concatena dos listas 
print(my_list + my_other_list) # [26, 24, 62, 52, 30, 30, 17, 26, 1.7, 'Matias', 'Benavides']


# trabajar con elementos de listas mutables ( otros elementos)
#que pasa si metemos otros elementos

my_other_list.append("AlilaAstrea") # Agrega un nuevo elemento inserta al final
print(my_other_list)

my_other_list.insert(1, "Rojo") # Dime el indice donde quieres insertar
print(my_other_list)

my_other_list[1] = "Celeste"  # cambio la posicion 1 por celeste
print(my_other_list)

my_other_list.remove("Celeste") # elimina el elemento de la lista
print(my_other_list)

my_list.remove(30)  # Solo a eliminado uno de los dos 30 y el primero del orden
print(my_list)


my_pop_element = my_list.pop(2)  # de esta forma guardamos el elemento eliminado en un lugar concreto

# print(my_list.pop(2))
print(my_pop_element)  
print(my_list)

del my_list[2] # elimina por indice # remove elimina el primero que encuentra
print(my_list) # desaparece el 52 sin guardarlo


my_new_list = my_list.copy() # el estado de la lista es una copia aparte



my_list.clear() # borra todo lo de la lista
print(my_list) 
print(my_new_list)


my_new_list.reverse() # Primero se llama reverse
print(my_new_list) # imprime los valores al revez [17, 30, 24, 26]


my_new_list.sort()  # sort ordena, indica criterios para ordenar
print(my_new_list)  # [17, 24, 26, 30] # lo ordena de mayor a valor

# pop() es para eliminar elemento pero quiero quedarmelo
# el uso habitual es para desapilar el ultimo elemento




#Tipos dinamicos

my_list = "Hola Python"
print(my_list)


"""
Ejercicios  

"""
# Declarar una lista vacía

listita = []
listota = list()

# Declarar una lista con más de 5 elementos

listita = [10, "pepe", 10.5, "azul", "banana"]

#Encuentra la longitud de tu lista

print(len(listita))

#Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.

primer = listita[0]
medio = listita[2]
ultimo = listita[4]
print(primer, medio, ultimo)

#Declare una lista llamada Mixed_data_types, ponga su (nombre, edad, altura, estado civil, dirección)

Mixed_data_types = ["Matias", 26, 1.70, "soltero", "Casita"]

#Declare una variable de lista llamada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Imprima la lista usando print()

print(Mixed_data_types)
print(it_companies)

#Imprimir el número de empresas de la lista.

nume = len(it_companies)
print("El numero de compañias son : ", nume)

#Imprimir la primera, mediana y última empresa.

first = it_companies[0]
mid = it_companies[3]
last = it_companies[6]

print(first, mid, last)

#Imprimir la lista después de modificar una de las empresas.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
modi = it_companies[0] = "elpepe"

print(it_companies)

#Agregar una empresa de TI a it_companies

it_companies.append("Github")
print(it_companies)

#Inserte una empresa de TI en medio de la lista de empresas.

it_companies.insert(3, "ManchadoCorp")
print(it_companies)

#Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)

it_companies[3] = it_companies[3].upper()   # Forma 1
print(it_companies)

it_companies[3] = 'MANCHADOCORP'            # Forma 2
print(it_companies)

#Únase a it_companies con una cadena '#; '

it_companies.insert(9, str('#;'))
print(it_companies)

#Compruebe si una determinada empresa existe en la lista it_companies.

existira = 'IBM' in it_companies
print(existira)  # True
existira = 'IBM me la come' in it_companies
print(existira) # False


#Ordenar la lista usando el método sort()

it_companies.sort()   # Antes ['elpepe', 'Google', 'Microsoft', 'MANCHADOCORP', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Github', '#;']
print(it_companies)   # ['#;', 'Amazon', 'Apple', 'Github', 'Google', 'IBM', 'MANCHADOCORP', 'Microsoft', 'Oracle', 'elpepe']

#Invierta la lista en orden descendente usando el método reverse()

it_companies.reverse()
print(it_companies)  # ['elpepe', 'Oracle', 'Microsoft', 'MANCHADOCORP', 'IBM', 'Google', 'Github', 'Apple', 'Amazon', '#;']

#Elimine las primeras 3 empresas de la lista

del it_companies[0:3]
print(it_companies) # ['MANCHADOCORP', 'IBM', 'Google', 'Github', 'Apple', 'Amazon', '#;']

#Elimine las últimas 3 empresas de la lista

del it_companies[4:7]
print(it_companies) # ['MANCHADOCORP', 'IBM', 'Google', 'Github']

#Elimine la empresa o empresas de TI intermedias de la lista

del it_companies[1:3]
print(it_companies) # ['MANCHADOCORP', 'Github']

#Eliminar la primera empresa de TI de la lista

del it_companies[0]
print(it_companies) # ['Github']

#Eliminar la empresa o empresas de TI intermedias de la lista

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

del it_companies[3] # delete Apple
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon']


#Eliminar la última empresa de TI de la lista

it_companies.remove('Amazon')
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle']

it_companies.pop() # eliminara el ultimo elemento pero seguira existiendo
print(it_companies)


#Eliminar todas las empresas de TI de la lista

it_companies.clear()
print(it_companies)

#Destruir la lista de empresas de TI

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

#print(it_companies) # NameError: name 'it_companies' is not defined / Confirma que esta borrada

try:
    print(it_companies)
except NameError as e:
    print(e)  # Salida: name 'it_companies' is not defined

#Únete a las siguientes listas:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

listas = front_end + back_end
print(listas) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print(front_end) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']




#Después de unirse a las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux.

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']  

#full_stack.extend(["Python", "SQL"]) # Esta opcion permite agregar los dos a la vez, pero no será donde especifica el ejercicio
#print(full_stack)

#Ejercicios: Nivel 2
#-------------------------------------------------------------------------------------------------------------#

#La siguiente es una lista de 10 edades de estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordena la lista y encuentra la edad mínima y máxima.

ages.sort()  # Forma 1

minima = ages[0]
maxima = ages[-1]

print(f"Lista de edad ordenada : ", ages)
print(f"Edad minima :", minima)
print(f"Edad maxima :", maxima)

#-------------------------------------------------------------------#

# Ordenar la lista de edades # Forma 2
ages_sorted = sorted(ages)  # python ordena automaticamente de menor a mayor la lista

# Encontrar la edad mínima y máxima
min_age = ages_sorted[0]  # el primer elemento
max_age = ages_sorted[-1]  # -1 siempre se refiere al ultimo elemento de la lista

# Imprimir los resultados
print(f"Lista de edades ordenada: {ages_sorted}")
print(f"Edad mínima: {min_age}")
print(f"Edad máxima: {max_age}")

"""

sort() modifica la lista original.
sorted() no modifica la lista original, sino que devuelve una nueva lista ordenada.

"""




#Agregue la edad mínima y la edad máxima nuevamente a la lista.


#Encuentre la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)

#Encuentre la edad promedio (suma de todos los artículos dividida por su número)

#Encuentra el rango de edades (máximo menos mínimo)

#Compare el valor de (min - promedio) y (max - promedio), use el método abs()

#Encuentre los países del medio en la lista de países

#Divida la lista de países en dos listas iguales si es incluso un país más para la primera mitad.

['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca'] 

#Desglose los primeros tres países y el resto como países escandinavos.