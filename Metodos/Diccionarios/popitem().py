'''Elimina y retorna el último par clave-valor.'''

dic = {'a': 1, 'b': 2}
item = dic.popitem()
print(dic)  # {'a': 1}
print(item)  # ('b', 2)
