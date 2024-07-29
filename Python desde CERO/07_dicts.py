### Dictionaries ### 

#Un diccionario es una colección de tipos de datos emparejados (clave: valor)
#  modificables (mutables) desordenados.

my_dict = dict()
print(type(my_dict)) # <class 'dict'>

my_other_dict = {}
print(type(my_other_dict)) # <class 'dict'> aunque simile un set


my_other_dict = {"Nombre":"Matias", "Apellido": "Benavides", "Edad": 26, 1: "Python"}

my_dict = {
    "Nombre": "Matias",
    "Apellido": "Benavides",
    "Edad": 26,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.71,
    }

print(my_other_dict)
# {'Nombre': 'Matias', 'Apellido': 'Benavides', 'Edad': 26, 1: 'Python'}
print(my_dict)
# {'Nombre': 'Matias', 'Apellido': 'Benavides', 'Edad': 26, 'Lenguajes': {'Kotlin', 'Swift', 'Python'}}

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

print(my_dict["Nombre"]) # Matias

my_dict["Nombre"] = "Javier"
print(my_dict["Nombre"]) # Javier ( actualiza la clave)

print(my_dict[1]) # 1.71

my_dict["Calle"] = "Calle AlilaAstrea" # Forma de agregar nuevo campo al dict
print(my_dict)
'''{'Nombre': 'Javier',
  'Apellido': 'Benavides',
    'Edad': 26,
      'Lenguajes': {'Swift', 'Python', 'Kotlin'},
        1: 1.71,
          'Calle': 'Calle AlilaAstrea'} '''

del my_dict["Calle"] # Forma de eliminar un solo elemento
print(my_dict)
'''{'Nombre': 'Javier',
  'Apellido': 'Benavides',
    'Edad': 26,
      'Lenguajes': {'Python', 'Swift', 'Kotlin'},
        1: 1.71} '''

print("Benavides" in my_dict) # False ( Buscamos por clave, no por valor)
print("Apellido" in my_dict) # True
print(my_dict["Apellido"]) # Benavides

print(my_dict.items()) # Tenemos listado de items
'''dict_items([('Nombre', 'Javier'),
             ('Apellido', 'Benavides'),
               ('Edad', 26),
                 ('Lenguajes', {'Kotlin', 'Swift', 'Python'}),
                   (1, 1.71)])'''

print(my_dict.keys()) # Retorna todas las claves
'''dict_keys(['Nombre',
            'Apellido',
              'Edad',
                'Lenguajes', 1])'''

print(my_dict.values()) # Retorna todos los valores
'''dict_values(['Javier',
              'Benavides',
                26,
                  {'Kotlin', 'Swift', 'Python'},
                    1.71])'''


my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Crea un diccionario nuevo sin valores
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
 
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}

my_new_dict = dict.fromkeys(my_dict, ("Matias", "Benavides"))
print(my_new_dict)
'''{'Nombre': ('Matias', 'Benavides'),
  'Apellido': ('Matias', 'Benavides'),
    'Edad': ('Matias', 'Benavides'),
      'Lenguajes': ('Matias', 'Benavides'),
        1: ('Matias', 'Benavides')}'''

my_new_dict = dict.fromkeys(my_dict, "AlilaAstrea")
print(my_new_dict) # Todos los valores son AlilaAstrea

print(list(my_new_dict.values())) # ['AlilaAstrea', 'AlilaAstrea', 'AlilaAstrea', 'AlilaAstrea', 'AlilaAstrea']
print(tuple(my_new_dict))
print(set(my_new_dict))

#-------------------------------------------------------------------#

# Si buscamos una clave que no existe dentro del diccionario nos dara error
# pero si usamos el metodo get para buscar en el diccionario nos dara un None al menos

my_dict = {
    "Nombre": "Matias",
    "Apellido": "Benavides",
    "Edad": 26,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.71,
    }


# print(my_dict["Felicidad"]) # KeyError: 'Felicidad'
print(my_dict["Nombre"]) # Matias
print(my_dict.get("Felicidad")) # None

# Existen dos formas de agregar claves y valores
my_dict["Juegos"] = ["Apex Legends", "SpiritFarer"]
print(my_dict)
# la función append() agrega un elemento al final de la lista y a un valor existente
my_dict['Juegos'].append('Stardew Valley') 

print(my_dict)
'''{'Nombre': 'Matias',
  'Apellido': 'Benavides',
    'Edad': 26,
      'Lenguajes': {'Python', 'Kotlin', 'Swift'},
        1: 1.71,
          'Juegos': ['Apex Legends', 'SpiritFarer', 'Stardew Valley']}'''


# Para remover una clave

my_dict.pop(1) # Elimina 1:1,71

my_dict.popitem() # Elimina Juegos

del my_dict["Lenguajes"] # Elimina Lenguajes

print(my_dict) # {'Nombre': 'Matias', 'Apellido': 'Benavides', 'Edad': 26}


my_dict = {
    'Nombre': 'Matias',
    'Apellido': 'Benavides',
    'Edad': 26,
    'Lenguajes': {'Python', 'Kotlin', 'Swift'},
    1: 1.71,
    'Juegos': ['Apex Legends', 'SpiritFarer', 'Stardew Valley']}

# El metodo items() cambia el diccionario a una lista de tuplas

print(my_dict.items())
'''dict_items([('Nombre', 'Matias'),
             ('Apellido', 'Benavides'),
               ('Edad', 26),
                 ('Lenguajes', {'Swift', 'Python', 'Kotlin'}),
                   (1, 1.71),
                     ('Juegos', ['Apex Legends', 'SpiritFarer', 'Stardew Valley'])])'''

# la funcion clear borra todos los elementos de la lista

print(my_dict.clear()) #None

# Eliminar diccionario
del my_dict


my_dict = {
    'Nombre': 'Matias',
    'Apellido': 'Benavides',
    'Edad': 26,
    'Lenguajes': {'Python', 'Kotlin', 'Swift'},
    1: 1.71,
    'Juegos': ['Apex Legends', 'SpiritFarer', 'Stardew Valley']}

# Podemos copiar el diccionario usando el metodo copy()

copia_dict = my_dict.copy()

print(copia_dict)
'''{'Nombre': 'Matias',
 'Apellido': 'Benavides',
   'Edad': 26,
     'Lenguajes': {'Python', 'Kotlin', 'Swift'},
       1: 1.71,
         'Juegos': ['Apex Legends', 'SpiritFarer', 'Stardew Valley']}'''

# El metodo keys() entrega todos las claves dentro del diccionario como una lista

claves = my_dict.keys()
print(claves) 
# dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1, 'Juegos'])

# El metodo values entrega todos los valores del diccionario como una lista

valores = my_dict.values()
print(valores) 
#dict_values(['Matias', 'Benavides', 26, {'Kotlin', 'Python', 'Swift'}, 1.71, ['Apex Legends', 'SpiritFarer', 'Stardew Valley']])


### Ejercicios -----------------------------------------------------------------------------### 

# Crea un diccionario vacío llamado perro

perrito = {}

# Agregue nombre, color, raza, patas y edad al diccionario de perros

perrito["Nombre"] = "Canela"
perrito["Color"] = "Verde Limon"
perrito["Raza"] = "Labrador"
perrito["Patas"] = 4
perrito["Edad"] = 6

print(perrito)
# {'Nombre': 'Canela',
#   'Color': 'Verde Limon',
#     'Raza': 'Labrador',
#       'Patas': 4,
#         'Edad': 6}

# Cree un diccionario de estudiantes y agregue nombre, apellido, sexo, edad, estado civil,
#  habilidades, país, ciudad y dirección como claves para el diccionario.

estudiantes = {
    "Nombre" : "Matias",
    "Apellido": "Benavides",
    "Sexo": "Hombre",
    "Edad": 26,
    "Estado Civil": "Corazon rotado",
    "Habilidades": ["Hechandole ganas a la vida", "Python", "MySQL"],
    "Pais": "Chile",
    "Ciudad": "Rancagua",
    "Direccion": "San ramonsito"
  
}



# Obtener la longitud del diccionario del estudiante

print(len(estudiantes)) # 9


# Obtenga el valor de las habilidades y verifique el tipo de datos, debería ser una lista

hablidades = estudiantes["Habilidades"]
print(hablidades) # ['Hechandole ganas a la vida', 'Python', 'MySQL']
print(type(hablidades)) # <class 'list'>


# Modifique los valores de las habilidades agregando una o dos habilidades.

estudiantes["Habilidades"].append("MongoDB")
print(estudiantes["Habilidades"]) 
# ['Hechandole ganas a la vida', 'Python', 'MySQL', 'MongoDB']

estudiantes["Habilidades"].extend(["Django", "Bootstrap"])
print(estudiantes["Habilidades"])
# ['Hechandole ganas a la vida', 'Python', 'MySQL', 'MongoDB', 'Django', 'Bootstrap']


# Obtenga las claves del diccionario como una lista

keys = estudiantes.keys()
print(list(keys))
# ['Nombre', 'Apellido', 'Sexo', 'Edad', 'Estado Civil', 'Habilidades', 'Pais', 'Ciudad', 'Direccion']

# Obtener los valores del diccionario como una lista

values = estudiantes.values()
print(list(values))
# ['Matias', 'Benavides', 'Hombre', 26, 'Corazon rotado', ['Hechandole ganas a la vida', 'Python', 'MySQL', 'MongoDB', 'Django', 'Bootstrap'], 'Chile', 'Rancagua', 'San ramonsito']
# Cambie el diccionario a una lista de tuplas usando el método items()


# Eliminar uno de los elementos del diccionario.

estudiantes.popitem()
print(estudiantes) # Elimino Dirección
# {'Nombre': 'Matias',
#   'Apellido': 'Benavides',
#     'Sexo': 'Hombre',
#       'Edad': 26,
#         'Estado Civil': 'Corazon rotado',
#           'Habilidades': ['Hechandole ganas a la vida', 'Python', 'MySQL', 'MongoDB', 'Django', 'Bootstrap'],
#             'Pais': 'Chile', 'Ciudad': 'Rancagua'}

# Eliminar uno de los diccionarios

del estudiantes
# print(estudiantes) 
# NameError: name 'estudiantes' is not defined

