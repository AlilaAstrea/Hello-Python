'''
Odd Or Even

Solicite un número al usuario. Dependiendo de si el número es par o impar,
imprima un mensaje apropiado para el usuario

Extras:

- Si el número es múltiplo de 4, imprima un mensaje diferente.

- Solicite al usuario dos números: un número para verificar (llámelo num) y un número para dividir por ( check).

- Si checkse divide uniformemente num, dígaselo al usuario. De lo contrario, imprima un mensaje apropiado diferente.


'''

number = int(input("Digite un numero: "))

if number % 2 == 0:
    print(f"{number} es par.")
elif number % 4 == 0:
    print(f"Este numero es múltiplo de 4")
else:
    print(f"{number} es impar.")


#-----------------------------------------------------------------#

user_num = int(input("Enter a number: "))

def oddoreven(number):
    if number % 2 == 0 and number % 4 != 0:
        print(f"The number {number} is even.")
    elif number % 2 == 0 and number % 4 == 0:
        print(f"The number {number} is even and is divisible by 4.")
    else:
        print(f"The number {number} is odd.")

oddoreven(user_num)