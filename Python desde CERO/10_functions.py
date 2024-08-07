### Functions ###


'''Una función es un bloque reutilizable de código o declaraciones de programación diseñadas
para realizar una determinada tarea. Para definir o declarar una función, Python proporciona
la palabra clave def. La siguiente es la sintaxis para definir una función.
El bloque de funciones de código se ejecuta solo si se llama o invoca la función.
'''

def my_function():
    print("Esto es una función")

my_function() # Esto es una función


#Dentro de parentesis podemos pasar parametros/argumentos

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5 , 7) # 12
sum_two_values(5345 , 12317) # 17662
sum_two_values("5" , "7") # 57 concatena cadenas de texto 
sum_two_values(1.4 , 5.2) # 6.6

my_result = sum_two_values(1.4, 5.2)
print(my_result) # None ya que no devuelve un dato la funcion (return)


#Tanto como recibe datos, puede retornar esos datos-------------------

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

# ya no hace un print, hace un return de la suma de los dos valores
#Para ser llamada se debe crear una variable

my_result = sum_two_values_with_return(10,5)
print(my_result) # Devuelve el valor 15


def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Benavides", name = "Matias") # Re ordena el orden de los prints
# Matias Benavides ( añadiendo parametros )

# PARAMETROS POR DEFECTO ------------------------------------------------
def print_name_with_default (name, surname, alias = "Sin Alias"): #Valor por defecto de alias
    print(f"{name} {surname} {alias}")

print_name_with_default("Matias", "Benavides", "AlilaAstrea")
# Matias Benavides AlilaAstrea
print_name_with_default("Matias", "Benavides")
#Matias Benavides Sin Alias

#Con el valor por defecto podemos llamar con o sin el parametro


def print_texts(*text): #Con asterisco podemos pasar cualquier parametro
    print(text)

print_texts("Hola", "Python", "AlilaAstrea")
# ('Hola', 'Python', 'AlilaAstrea')
print_texts("Hola")
# ('Hola',)

def print_texts(*texts): #Con asterisco podemos pasar cualquier parametro
    for text in texts:
        print(text.upper())


# Una funcion con parametros arbitrarios, ya que los parametros que pasamos no son una lista
# y lo devuelve como tál
print_texts("Hola", "Python", "AlilaAstrea")
print_texts("Hola")
# HOLA
# PYTHON
# ALILAASTREA
# HOLA


# ------------------------------------------------------------------------------------------------



# FUNCIÓN SIN PARAMETROS
# Una funcion puede declararse sin parametros

#Ejemeplo:

def generate_full_name ():
    first_name = 'Matias'
    last_name = 'Benavides'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function
# Matias Benavides

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
# 5

# FUNCIÓN QUE DEVUELVE UN VALOR 
'''
La función también puede devolver valores; si una función no tiene una declaración de
devolución, el valor de la función es None. Reescribamos las funciones anteriores usando
return. De ahora en adelante, obtenemos un valor de una función cuando la llamamos y la
imprimimos.
'''

def generate_full_name ():
    first_name = 'Matias'
    last_name = 'Benavides'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
# Matias Benavides

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
# 5


# FUNCIÓN CON PARAMETROS
'''
En una función podemos pasar diferentes tipos de datos
(number, string, boolean, list, tuple, dictionary o set) como parámetro
'''
'''
Parámetro único: si nuestra función toma un parámetro,
debemos llamar a nuestra función con un argumento

  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
  '''

# Ejemplo:
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Matias'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


'''
Dos parámetros: una función puede tener o no un parámetro o parámetros. Una función también puede tener dos o más parámetros. Si nuestra función toma parámetros, deberíamos llamarla con argumentos. Comprobemos una función con dos parámetros:
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
'''
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Matias','Benavides'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2024, 1997))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


# PASAR ARGUMENTOS CON CLAVE Y VALOR 
'''
Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
'''

# Ejemplo:
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Matias', lastname = 'Benavides')

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2 = 3, num1 = 2) # Order does not matter


# FUNCIÓN QUE DEVUELVE UN VALOR (2)
'''
Si no devolvemos un valor con una función, entonces nuestra función devuelve Ninguno de forma predeterminada. Para devolver un valor con una función usamos la palabra clave return seguida de la variable que estamos devolviendo. Podemos devolver cualquier tipo de datos desde una función.
'''

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2024, 1997))


# Ejemplo de retornar un booleano

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

# Ejemplo de retornar una lista

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10)) # [0, 2, 4, 6, 8, 10]


# FUNCIÓN CON PARAMETRES POR DEFECTO
'''
A veces pasamos valores predeterminados a los parámetros cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
'''

# Ejemplo
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) # Peter, welcome to Python for Everyone!
print(greetings('Matias')) # Matias, welcome to Python for Everyone!

def generate_full_name (first_name = 'Matias', last_name = 'Benavides'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2024):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1997))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon


# NÚMERO ARBITRARIO DE ARGUMENTOS
'''
Si no sabemos la cantidad de argumentos que pasamos a nuestra función, podemos crear una función que pueda tomar una cantidad arbitraria de argumentos agregando * antes del nombre del parámetro.
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
'''

# Ejemplo:
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

# Número predeterminado y arbitrario de parámetros en funciones

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Matias','Benavides','Javier','Rojas')

# Función como parámetro de otra función

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 4)) # 16


# Ejercicios --------------------------------------------------------------------------------#


# Declarar una función add_two_numbers. Toma dos parámetros y devuelve una suma.

# El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule el área_del_círculo.

# Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos. Compruebe si todos los elementos de la lista son tipos numéricos. Si no, dé una valoración razonable


# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit.

# Escribe una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano


# Escribe una función llamada calcular_pendiente que devuelva la pendiente de una ecuación lineal.

# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn.

# Declare una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.

# Declare una función llamada lista_inversa. Toma una matriz como parámetro y devuelve el reverso de la matriz (use bucles).
'''
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
'''


# Declare una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve una lista de elementos en mayúscula

# Declare una función llamada add_item. Se necesita una lista y parámetros de un elemento. Devuelve una lista con el elemento agregado al final.
'''
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
'''

# Declare una función llamada remove_item. Se necesita una lista y parámetros de un elemento. Devuelve una lista con el elemento eliminado.
'''
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
'''

# Declare una función llamada suma_de_números. Toma un parámetro numérico y suma todos los números en ese rango.
'''
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
'''


# Declare una función llamada suma_de_probabilidades. Toma un parámetro numérico y suma todos los números impares en ese rango.

# Declare una función llamada suma_de_pares. Toma un parámetro numérico y suma todos los números pares en ese rango.


# Ejercicios lvl 2 -------------------------------------------------------------------------

# Declare una función llamada pares_y_odds. Toma un número entero positivo como parámetro y cuenta el número de pares y impares en el número.
'''
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
'''


# Llame a su función factorial, toma un número entero como parámetro y devuelve un factorial del número

# Llame a su función is_empty, toma un parámetro y verifica si está vacía o no

# Escribe diferentes funciones que tomen listas. Deben calcular_media, calcular_mediana, calcular_modo, calcular_rango, calcular_varianza, calcular_estándar (desviación estándar).


# Ejercicios lvl 3  -------------------------------------------------------------------------

# Escribe una función llamada is_prime, que verifique si un número es primo.


# Escriba una función que verifique si todos los elementos son únicos en la lista.

# Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.

# Escriba una función que verifique si la variable proporcionada es una variable de Python válida


# Vaya a la carpeta de datos y acceda al archivo países-data.py.


# Crea una función llamada most_spoken_languages ​​in the world. Debería devolver 10 o 20 idiomas más hablados en el mundo en orden descendente.


# Cree una función llamada países_más_poblados. Debería devolver 10 o 20 países más poblados en orden descendente.
