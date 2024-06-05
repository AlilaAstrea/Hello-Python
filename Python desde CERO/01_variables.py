# Variables

# MyVariable = "My String variable"  #Forma indevida, más no incorrecta
# print(MyVariable)

my_string_variable = "My String variable"  # Forma optima
print(my_string_variable)

my_int_variable = 4
print(my_int_variable)

my_int_to_str_variable =str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


#Print puede llevar diferentes argumentos
# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

print("Este es el valor de: ", my_bool_variable) #concateno ambos datos

# Funciones del sistema

# len() cuenta los caracteres contando hasta los espacios
print(len(my_int_to_str_variable))  # : 1
print(len(my_string_variable))      # : 18

# Variables en una sola línea. ¡No abusar de la sintaxis!
name, surname, alias, age = "Matias", "Benavides", "Alila", 26

print("Me llamo:", name, surname,"Mi edad es:", age,"Y mi alias es:", alias)
# : Me llamo: Matias Benavides Mi edad es: 26 Y mi alias es: Alila

# Inputs
# sistema de input, para la ejecución hasta que respondas

""""
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)
"""""

# Cambiamos su tipo

name = 123
age = "Matias"
print(name)
print(age)


# Forzamos el tipo
address: str = "Mi dirección"
address = 32
print(address)   # 32 y el tipo es int (se sobreescribio)
