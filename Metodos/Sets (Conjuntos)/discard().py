'''Elimina un elemento, si no existe no lanza error.'''

s = {1, 2, 3}
s.discard(2)
print(s)  # {1, 3}
