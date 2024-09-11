
''' 
Issubset()
Devuelve True si todos los elementos del conjunto están presentes en otro conjunto (el argumento), False en caso contrario.
'''

a ={1,2,3}
b ={1,2,3,4,5}
c ={1,2,4}

print(a.issubset(b)) #output = True
print(a.issubset(c)) #output = False