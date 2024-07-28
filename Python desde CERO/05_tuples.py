### Tuplas ###

"""
Una tupla es una colección de diferentes tipos de datos que está ordenada y
 es inmutable (inmutable). Las tuplas se escriben entre corchetes, ().
   Una vez creada una tupla, no podemos cambiar sus valores. No podemos usar métodos agregar, insertar y eliminar en una tupla porque no es modificable (mutable). A diferencia de la lista, la tupla tiene pocos métodos.

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

# Ejercicios #

# Crea una tupla vacia
latupla = ()

# Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)

latupla = ("Mackarena", "Juan Pablo", "Mario")

# Únase a tuplas de hermanos y hermanas y asígnelas a hermanos

brothers = ("Juan Pablo", "Mario")

sisters = ("Mackarena",) 

siblings = brothers + sisters
print(siblings) # ('Juan Pablo', 'Mario', 'Mackarena')

"""""
# Esto es una cadena
sisters = ("Mackarena")  # Tipo: str

# Esto es una tupla con un solo elemento
sisters = ("Mackarena",)  # Tipo: tuple
"""""
# ¿Cuántos hermanos tiene usted?

print(len(siblings)) # 3

# Modifica la tupla de hermanos y agrega el nombre de tu padre y tu madre y asígnalo a family_members

family_members = list(siblings)
print(type(family_members))

#family_members.insert(0, "Juan")
#family_members.insert(1, "Adriana")

padres = ["Juan", "Adriana"]
family_members.extend(padres)

print(family_members) #['Juan Pablo', 'Mario', 'Mackarena', 'Juan', 'Adriana']

# Desempaquetar hermanos y padres de family_members

(joven, adulto, pequeña, viejo, abuela) = family_members
print(joven) # Juan Pablo
print(adulto) # Mario
print(pequeña) # Mackarena
print(viejo) # Juan
print(abuela) # Adriana

# Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.

frutas = ("manzana", "banana", "pera", "sandia")
verduras = ("tomate", "zanahoria", "papa", "cebolla")
producto_animal = ("t-bone","guachalomo", "panita", "tuto de pollo")

food_stuff_tp = frutas + verduras + producto_animal
print(food_stuff_tp) # ('manzana', 'banana', 'pera', 'sandia', 'tomate', 'zanahoria', 'papa', 'cebolla', 't-bone', 'guachalomo', 'panita', 'tuto de pollo')

# Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_tl = list(food_stuff_tp)
print(type(food_stuff_tl)) # <class 'list'>


# Corte el elemento o elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.

print(food_stuff_tp[5:12]) #['zanahoria', 'papa', 'cebolla', 't-bone', 'guachalomo', 'panita', 'tuto de pollo']

#Corte los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt

print(food_stuff_tl[3:12], food_stuff_tl[-3:12])
# ['sandia', 'tomate', 'zanahoria', 'papa', 'cebolla', 't-bone', 'guachalomo', 'panita', 'tuto de pollo']
# ['guachalomo', 'panita', 'tuto de pollo']

# Eliminar completamente la tupla food_staff_tp
del food_stuff_tp
#print(food_stuff_tp) # NameError: name 'food_stuff_tp' is not defined.

# Compruebe si existe un elemento en tupla:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("Estonia es un pais nordico")
else:
    print("Estonia no es un pais nordico")

if 'Iceland' in nordic_countries:
    print("Iceland es un pais nordico")
else:
    print("Iceland no es un pais nordico")

