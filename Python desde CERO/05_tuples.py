### Tuplas ###

"""
Una tupla es una colección de diferentes tipos de datos que está ordenada y es inmutable (inmutable). Las tuplas se escriben entre corchetes, (). Una vez creada una tupla, no podemos cambiar sus valores. No podemos usar métodos agregar, insertar y eliminar en una tupla porque no es modificable (mutable). A diferencia de la lista, la tupla tiene pocos métodos.

"""

my_tuple = tuple() # Si no metes el constructor de clase lo tomaria como una lista, este al decir tuple ya lo relaciona a una tupla aunque la sintaxis sea similar al de la lista
my_other_tuple = ()

my_tuple = (35, 1.71, "Matias", "Benavides", "Matias")
my_other_tuple = (35, 60, 30)

print(type(my_tuple))  # <class 'tuple'>

print(my_tuple[0]) # 35
print(my_tuple[-1]) # Benavides

tp1 = ('item1', 'item2', 'item3')
print(len(tp1)) # 3

print(my_tuple.count("Matias")) # 2
print(my_tuple.index("Benavides")) # 3 ( Indice de 0,1,2,"3")
print(my_tuple.index("Matias")) # 2

# my_tuple[1] = 1.80 
# print(my_tuple) # Da error, porque las tuplas no pueden cambiar su valor. (Inmutable)
                # 'tuple' object does not support item assignment

print(my_tuple + my_other_tuple) # (35, 1.71, 'Matias', 'Benavides', 'Matias', 35, 60, 30)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # ('Benavides', 'Matias', 35)
                         # Buscamos elemento del indice 3 y el 6

my_tuple = list(my_tuple)
print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "Alila"
my_tuple.insert(1, "Celeste")
my_tuple = tuple(my_tuple)  
print(my_tuple) # (35, 'Celeste', 1.71, 'Matias', 'Benavides', 'Alila')
print(type(my_tuple)) # <class 'tuple'>


# no queremos que cambie Tupla, si queremos que cambie entonces Lista.

#del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

#del my_tuple

#print(my_tuple) # NameError: name 'my_tuple' is not defined

#---------------------------------------------------------------------------------------#




