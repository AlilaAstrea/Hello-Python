'''Combina varios iterables en pares.'''

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = zip(lista1, lista2)
print(list(combinada))  # [(1, 'a'), (2, 'b'), (3, 'c')]



nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
combinado = zip(nombres, edades)
print(list(combinado))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
