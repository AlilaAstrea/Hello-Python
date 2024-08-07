### Classes ###
# estructura de programación que permite definir un conjunto de métodos y atributos que describen un objeto o entidad.

# El concepto de poder identificar nuestro codigo dentro de un habito de actuacion


class MyEmptyPerson:
    pass
# pass indica al programa que ignore esa condición y continúe ejecutando el programa como de costumbre

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    # __init__ nos sirve para crear un constructor de clase
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
# self si queremos crear una clase que tenga un constructor le tenemos que pasar self. self se refiere a la instancia de 'el mismo'
# En este caso asignamos name a una propiedad llamada name que se especifico en el __init__

# Propiedad name y parametro name

my_person = Person("Matias", "Benavides")
print(my_person.name) # Matias

print(f"{my_person.name} {my_person.surname}") # Matias Benavides


#Pasar datos sin parametros y definirlos dentro del cosntructor

class Persona:
    def __init__(self):
        self.name = "Matiti"
        self.surname = "Javier"

my_persona = Persona()
print(f"{my_persona.name} {my_persona.surname}") # Matiti Javier

#Crear una propiedad almacenada

class Personita:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

my_personita = Personita("Javier", "Rojas")
print(my_personita.full_name)


#---------------------------------------------------------------#
#Agregar funciones

class Personita:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name # Propiedad privada

    def walk(self):
        print(f"{self.full_name} Está caminando")

my_personita = Personita("Javier", "Rojas")
print(my_personita.full_name) # Javier Rojas (Sin alias)
my_personita.walk()  # Javier Rojas (Sin alias) Está caminando

my_other_person = Personita("Matita", "Benavita", "Alita")
print(my_other_person.full_name) # Matita Benavita (Alita)
my_other_person.walk() # Matita Benavita (Alita) Está caminando

my_other_person.full_name = "Elpepe (etesech)"
print(my_other_person.full_name) # Elpepe (etesech)



