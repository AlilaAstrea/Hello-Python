'''Devuelve True si todos los elementos de un iterable son True.'''

valores = [1, 2, 3]
print(all(valores))  # True

valores2 = [1, 0, 3]
print(all(valores2))  # False
