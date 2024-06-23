### Lists ###



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