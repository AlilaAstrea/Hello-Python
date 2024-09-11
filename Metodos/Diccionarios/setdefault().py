'''Retorna el valor de una clave, si no existe añade la clave con un valor predeterminado.'''


dic = {'a': 1}
dic.setdefault('b', 2)
print(dic)  # {'a': 1, 'b': 2}
