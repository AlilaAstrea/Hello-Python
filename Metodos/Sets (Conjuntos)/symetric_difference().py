'''Retorna los elementos que están en un set o en el otro, pero no en ambos.'''

s1 = {1, 2}
s2 = {2, 3}
print(s1.symmetric_difference(s2))  # {1, 3}
