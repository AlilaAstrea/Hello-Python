### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))  # 9
print(len(my_other_string)) # 14

print(my_other_string +"   "+ my_string)

# Los string pueden llevar ciertos caracteres

my_new_line_string = "Este es un String\ncon salto de línea" # \n (Salto de linea)
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Mete un TAB
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" # Hace tab y salto de linea
print(my_scape_string)   # \\ no hace caso al tab (\t) o al salto de linea con \\n


# Formateo

name, surname, age = "Matias", "Benavides", 26

# %s es : Que el primer texto que yo le pase formateado a esta cadena lo metera
# %s - String y %d para Integers

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Mi nombre es Matias Benavides y mi edad es 26
# Con .format debes dejar llaves {}
# con %s o %d . Agregas el % con las variables a su lado

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # La mejor forma


# Desempaquetado de caracteres
 
language = "python"

#Toma la palabra Python con caracteres contados del 0 al 5, osea
# ['P','y','t','h','o','n']
#   0   1   2   3   4   5

a, b, c, d, e, f = language   
print(a)  # P
print(b)  # y

primera_letra = language[0]
print(primera_letra) # P
segunda_letra = language[1]
print(segunda_letra) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


# División

language_slice = language[1:3] # cuenta desde 1 hasta 3
# contempla el 0 = P entonces
# 0= P, 1= y, 2= t, 3= h 
print(language_slice) #yt

language_slice = language[1:]
print(language_slice) #ython

language_slice = language[-2]
print(language_slice) #o

language_slice = language[0:6:2]  # Muestra el caracter de cada posicion
print(language_slice) #Pto  # slicing

# Reverse

reversed_language = language[::-1]  # el final empieza por -1
print(reversed_language) # nohtyP

# Funciones

print(language.capitalize()) # pone mayuscula la palabra
print(language.upper())  # PYTHON en mayus
print(language.count("t")) # Cuenta el caracter
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.lower()) # Tode minuscula
print(language.upper().isupper()) #.isuper es para comprobar si esta en mayus # True / si fuera lower.isupper daria False
print(language.startswith("py")) # Si empieza con tal caracter / # True


# Ejercicios 

# Concatena el string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'

oracion = [ "Thirty", "Days", "Of", "Python"]
resultado = ' '.join(oracion)  # El ' ' contiene un espacio que lo incluye al final de cada elemento 
print(resultado) # Thirty Days Of Python

# Concatena el string 'Coding', 'For', 'All' to a single string, ' Coding For All'

conc = ["Coding", "For", "All"]
resu = ' '.join(conc)
print(resu) # Coding For All

# Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
# Imprime la variable empresa utilizando print().

empresa = "Codificación para todos"
print(empresa)

# Imprime la longitud de la cadena de la empresa utilizando el método len() y print().

print(len(empresa)) # 23 ( cuenta espacios )

# Cambia todos los caracteres a mayúsculas utilizando el método upper().
print(empresa.upper()) # CODIFICACIÓN PARA TODOS

# Cambia todos los caracteres a minúsculas utilizando el método lower().
print(empresa.lower()) # codificación para todos

# Utiliza los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All.
print(resu.capitalize())
print(resu.title())
print(resu.swapcase())

# Corta la primera palabra de la cadena Coding For All. 9°
