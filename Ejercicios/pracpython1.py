'''
Character Input 

Crear un programa que pida al usuario que introduzca su nombre y su edad. Imprime un mensaje dirigido a ellos que les indique el año en que cumplirán 100 años. Nota: para este ejercicio, la expectativa es que escriba explícitamente el año (y, por lo tanto, quede desactualizado el año siguiente). 

'''

nombre = input("Escribe tu nombre : ")
año = int(input("Digita tu año de nacimiento : "))

# Año en el cumplo 100 de edad
año_cien = año + 100
print(f"{nombre}, en el año {año_cien} cumplirás 100 años.")


currentYear = 2024
nameU = input("What is your name?")
ageU = int(input("How old are you?"))
yearAge100 = currentYear - ageU + 100
print("{0}, you will turn 100 years old in the year {1}!".format(nameU,yearAge100))


