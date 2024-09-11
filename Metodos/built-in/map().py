'''Aplica una función a cada elemento de un iterable (como una lista).'''

numeros = [1, 2, 3, 4]

def cuadrado(n):
    return n * n

resultado = map(cuadrado, numeros)
print(list(resultado))  # [1, 4, 9, 16]
