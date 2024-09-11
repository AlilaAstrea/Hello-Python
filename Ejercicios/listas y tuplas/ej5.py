'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

'''

numeros= [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()
for numero in numeros:
    print(numero, end=", ")

# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 

# print(numeros) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


