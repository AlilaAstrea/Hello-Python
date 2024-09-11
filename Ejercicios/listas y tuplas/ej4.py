'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

ganadores = []

for i in range(6):  # Metodo range para hacer varias validaciones
    ganadores.append(int(input("Introduce un número ganador: ")))
ganadores.sort()

print(f"Los números ganadores son  {str(ganadores)}" )