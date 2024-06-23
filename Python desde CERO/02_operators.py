## Operadores ##

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

print(10 % 3) # Operador de modulo es que establescamos una division
              # y saber cual es el resto que tenemos
              # para saber si hay un multiplo por ej 
print( 2 ** 3) # Exponente osea 3 * 3 * 3

print( 10 // 3) # Floor division ( division aproximada a un numero entero)

print("Hola" + " Python")
#print("Hola" + 5) #TypeError: can only concatenate str (not "int") to str

print("Hola " + str(5))

print(2 ** 3 + 3 - 7 / 1 // 4)

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)  #Bool operador logico que sirve para ver si es True or False
print(3 < 4)   # True
print(3 >= 4)  # False
print(4 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True
print(3 > 4 > 2)


print("Hola" > "Python")  
print("Hola" < "Python")   
print("Hola" >= "Zola") # Ordenación alfabética    
print("Hola" <= "Python")  
print("Hola" == "Hola")     
print("Hola" != "Python")


### Operadores Lógicos ###
#logica booleana rige toda la programacion

print(3 > 4 and "Hola" > "Python")  
print(3 > 4 or "Hola" > "Python") 
print(3 < 4 and "Hola" < "Python")  
print(3 < 4 or "Hola" > "Python" and 4 == 4) 
#print(3 > 4 not "Hola" > "Python") 

print(not(3 > 4))  # el not es para negar toda la condición (diria False)
                    # Con el not da True 


### Ejercicios ###

# escribe un script para que el usuario ingrese la base y la altura de un triangulo y calcule el are de este traingulo = area ( 0.5 x b x h)

"""
base = int(input("Base de el triangulo: "))
altura = int(input("Altura de el triangulo: "))
area = base * altura
print("El area del triangulo es : ", area * 0.5)
print("Felicidades!")

base = 20
altura = 10
area = base * altura
print("El area del triangulo es ", area * 0.5)
"""

#----------------------------------------------------#
# Escribe un script que pida al usuario que ingrese el lado a, el ladob, y el lado c del triangulo. Calcula el perimetro del triangulo ( perimetro = a + b + c)

a = int(input("Ingrese el lado a del triangulo :"))
b = int(input("Ingrese el lado b del triangulo :"))
c = int(input("Ingrese el lado c del triangulo :"))

print("El perimetro del triangulo es : ", a + b + c)

#--------------------------------------------------#
# Obtén la longitud y el ancho de un rectangulo usando un prompt. Calcula su area ( area = longitud x ancho) y su perimetro ( perimetro = 2 x (longitud + ancho) )

long = int(input("Ingrese longitud del rectangulo : "))
anch = int(input("Ingrese ancho del rectangulo : "))
area = long * anch
perimetro = 2 * (long + anch)
print("El area del rectangulo es : ", area, " \n  Y su perimetro es de : ",perimetro )

#-------------------------------------------------------#
# Obtén el radio de un circulo usando un prompt. Calcula el área ( area = pi x r x r) y la circunferencia ( c = 2 x pi x r) donde pi = 3.14

pi = 3.14

longi = int(input("Ingresa la longitud del circulo : " ))
print("El radio de un circulo es : ", longi / (2 * pi))
print("Su área es de : ", pi * (longi / (2 * pi) * (longi / (2 * pi))))
print(" Y circunferencia es de : ", 2 * pi * (longi / (2 * pi)))

#r = C / 2*pi

#---------------------------------------------------------------#


