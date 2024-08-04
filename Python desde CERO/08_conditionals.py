###  Conditionals ###

# Establece flujos de ejecución de nuestro codigo
# Definir si algo se ejecutara o no.

'''De forma predeterminada, las declaraciones en el script Python se ejecutan secuencialmente
 de arriba a abajo. Si la lógica de procesamiento así lo requiere, el flujo secuencial de
 ejecución se puede alterar de dos maneras:


- Ejecución condicional: se ejecutará un bloque de una o más declaraciones si una
 determinada expresión es verdadera

- Ejecución repetitiva: un bloque de una o más declaraciones se ejecutará repetitivamente
 siempre que una determinada expresión sea verdadera. En esta sección, cubriremos
 las declaraciones if, else, elif. Los operadores lógicos y de comparación que
 aprendimos en las secciones anteriores serán útiles aquí'''


# La palabra clave if se usa para verificar si una condición es verdadera y ejecutar el código de bloque


# if condicion:
#     esta parte de codigo corre en condiciones verdaderas

a = 3
if a > 0:
    print("A es un numero positivo")

my_condition = True # (False) 

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

# Imprime ambas condiciones al ser Verdadero (True)
# Si es False la condicion 'my_condition' esta ejecutara el segundo print

my_condition = 5 * 5 # 3

if my_condition == 10: # Si fuera 10 daria True, por ende el primer print
    print("Se ejecuta la condicipon del segundo if") # No se ejecuta ya que no es verdadero


# if else dicta de que si no se cumple la primera condicion (if) debera cumplirse la segunda (else)
# en otros terminos es decir "si y de lo contrario" o "si y por ende"
if my_condition > 10 and my_condition < 20:      
    print("Es Mayor que 10 y menor que 20")
elif my_condition == 25: # Elif necesita una condicion, no puede escribirse como el else: 
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")


# ------------------------------------------------------------------------------------------------

a = 0 
if a > 0:
    print("A es un numero positivo")
elif a < 0:
    print("A es un numero negativo")
else:
    print("A es cero") # A es cero

# Short Hand
# code if condicion else code 

a = 3 
print("A es positivo") if a > 0 else print("A es negativo") # A es positivo

# Las condiciones se puede anidar
# if condicion:
#     code
#     if condicion:
#     code

a = 0
if a > 0:
    if a % 2 == 0:
        print("A es positivo y tambien par") # Si es 2 o par lo imprime
    else:
        print("A es un numero positivo") # Si es positivo o impar imprime
elif a == 0:
    print("A es cero") # Si a = 0 lo imprime
else:
    print("A es un numero negativo") # Si es -1 o -x imprime


# Podemos evitar condiciones anidadas con el operador logico 'and'
# if condicion and condicion:
#     code

a = 0
if a > 0 and a % 2 == 0:
    print("A es un numero entero par y positivo") # Si es 2, 4 , 6 etc
elif a > 0 and a % 2 != 0:
    print("A es un entero positivo") # Si no es par: 3 , 5, 7 etc
elif a == 0:
    print("A es cero") # al poner 0
else:
    print("A es negativo") # Si pones -1 -(numero)


# Operador logico if and or
# if condicion or condicion:
#     code

usuario = "Jaime"
nivel_acceso = 3
if usuario == 'admin' or nivel_acceso >= 4:
    print("Acceso Permitido")
else:
    print("Acceso Denegado")


# Ejercicios ---------------------------------------------------------#

# Obtenga información del usuario mediante input ('Ingrese su edad:').
#  Si el usuario tiene 18 años o más, envíe su opinión: tiene edad suficiente para conducir.
#  Si tiene menos de 18 años, envíe su opinión para esperar la cantidad de años que faltan.
#  Producción:
'''Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.'''

edad = int(input("Ingrese Su edad : "))

if edad >= 18:
    print("Tiene edad suficiente para conducir")
elif edad == 15:
    print("Necesitas 3 años más para aprender a conducir")
else:
    print("Eres un bebe, aun no estas listo")


# Compare los valores de my_age y your_age usando if... else. ¿Quién es mayor (tú o yo)?
#  Utilice input(“Ingrese su edad: ”) para obtener la edad como entrada. Puede utilizar
#  una condición anidada para imprimir 'año' para una diferencia de edad de 1 año, 'años'
#  para diferencias mayores y un texto personalizado si mi_edad = su_edad. Producción:
'''Enter your age: 30
You are 5 years older than me.'''

mi_edad = int(input("Ingresa mi edad (2°): "))
tu_edad = int(input("Ingresa tu edad (2°): "))

if mi_edad == tu_edad:
    print("Tenemos la misma edad.")
elif mi_edad > tu_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print("Tú eres 1 año mayor que yo.")
    else:
        print(f"Tú eres {diferencia} años mayor que yo.")

'''mi_edad = int(input("Ingresa mi edad (2°) :"))
tu_edad = int(input("Ingresa tu edad (2°) :"))

if mi_edad and tu_edad >= 18:
    if mi_edad == 26 and tu_edad == 26:
        print("Eres mayor de edad y tenemos la misma edad")
    elif tu_edad == 25 and mi_edad == 26:
        print("Tenemos una diferencia de un año")
    else:
        print("Al menos tienes 18")
    
    if tu_edad + 2 > mi_edad : 
        print("Me pasas por algunos años") 

elif mi_edad > tu_edad < 18:
    print("Aun no pasas los 18 años")

else:
    print("Eres menor de 18 años")'''
    
# Obtenga dos números del usuario mediante el mensaje de entrada. Si a es mayor que b,
#  devuelve a es mayor que b, si a es menor que b, devuelve a es menor que b;
#  de lo contrario, a es igual a b. Producción:
''' Enter number one: 4
    Enter number two: 3
    4 is greater than 3'''

a = int(input("Ingrese el numero A : "))
b = int(input("Ingrese el numero B : "))

if a == b:
    print("Son los mismos numeros")
elif a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es menor que {b}")


### Exercises: Level 2----------------------------------------------------------------------


# Escriba un código que califique a los estudiantes según sus puntuaciones:
''' 90-100, A
    70-89,  B
    60-69,  C
    50-59,  D
    0-49,   F'''

estudiante = int(input("Ingrese su calificación : "))

if estudiante > 100:
    print(f"Su calificación {estudiante} es mayor que 100. ¿Hizo trampa?")
elif estudiante >= 90 and estudiante <= 100:
    print(f"Su calificación de {estudiante} es A, Felicidades, sigue así!")
elif estudiante >= 70 and 89:
    print(f"Su calificación de {estudiante} es B, Un poco más y lo harás mejor!!")
elif estudiante >= 60 and 69:
    print(f"Su calificación de {estudiante} es C, Muy Bien!")
elif estudiante >= 50 and 59:
    print(f"Su calificación de {estudiante} es D, Buen intento, la siguiente será mejor")
elif estudiante >= 0 and 49:
    print(f"Su calificación de {estudiante} es F, Mejorarás!")
else:
    print("No calificas a una nota, el maximo es 100 :/")


# Consulta si la temporada es Otoño, Invierno, Primavera o Verano.
#  Si la entrada del usuario es: septiembre, octubre o noviembre, la temporada es otoño.
#  Diciembre, enero o febrero, la temporada es invierno. Marzo, abril o mayo,
#  la temporada es primavera Junio, julio o agosto, la temporada es verano

# otoño = ["septiembre","octubre","noviembre"]
# invierno = ["diciembre","enero","febrero"]
# primavera = ["marzo","abril","mayo"]
# verano = ["junio","julio","agosto"]

temporada = {
    "Otoño": ["septiembre","octubre","noviembre"],
    "Invierno": ["diciembre","enero","febrero"],
    "Primavera": ["marzo","abril","mayo"],
    "Verano": ["junio","julio","agosto"]
}

consulta = input("Ingrese un mes : ")

if consulta in temporada["Otoño"]:  # in hará que consulte dentro de la lista , al contrario si es con == este consultara a la lista completa
    print("La temporada es Otoño")
elif consulta in temporada["Invierno"]:
    print("La temporada es Invierno")
elif consulta in temporada["Primavera"]:
    print("La temporada es Primavera")
elif consulta in temporada["Verano"]:
    print("La temporada es Verano")
else:
    print("Indique un mes apto")




# La siguiente lista contiene algunas frutas:

# Si una fruta no existe en la lista, agregue la fruta a la lista e imprima la lista
# modificada. Si la fruta existe print('Esa fruta ya existe en la lista')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append("pepita")
print(fruits)

fruta = input("Agregue una fruta a la Lista :")

if fruta in fruits:
    print("Esta fruta ya existe en la lista")
elif fruta:
    fruits.append(fruta)
    print("Se agrego la fruta correctamente")
    print(f"{fruits} Acá esta!")
else:
    print("No está aca mish")


# Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!



person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Verifique si el diccionario de la persona tiene claves de habilidades; de ser así,
#  imprima la habilidad intermedia en la lista de habilidades.

habilida = person["skills"]
print(habilida[2:3])

if person in person["skills"]:
    print("Tiene habilidades")
else:
    print("No tiene habilidades")




# * Verifique si el diccionario de la persona tiene la clave de habilidades; de ser así,
#  verifique si la persona tiene la habilidad 'Python' e imprima el resultado.

# * Si una persona tiene habilidades solo JavaScript y React, imprima
#  ('Él es un desarrollador front-end'), si la persona tiene habilidades Node, Python,
#  MongoDB, imprima ('Él es un desarrollador backend'), si la persona tiene habilidades React,
#  Node y MongoDB, Print('Es un desarrollador fullstack'), de lo contrario 
# print('título desconocido'): para obtener resultados más precisos, se pueden anidar más
#  condiciones.

# # * Si la persona está casada y vive en Finlandia, imprima la información en el siguiente
#  formato: