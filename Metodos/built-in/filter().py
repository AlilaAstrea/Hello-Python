'''Filtra los elementos de un iterable, dejando solo los que cumplen una condición.'''

numeros = [1, 2, 3, 4, 5, 6]

def es_par(n):
    return n % 2 == 0

resultado = filter(es_par, numeros)
print(list(resultado))  # [2, 4, 6]
