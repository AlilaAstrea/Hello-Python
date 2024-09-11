'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

asignatura = ["Matemáticas", "Física","Química","Historia","Lengua"]
notas = []

for asig in asignatura:
    nota = input(f"¿Qué nota has sacado en {asig} ?" )
    notas.append(nota)
for i in range(len(asignatura)):
    print(f"En {asignatura[i]} has sacado {notas[i]}")

# el primer for recorre asignatura y se agrega una variable que guarda un input preguntando por que nota a sacado en cada una de las materias de la lista.
# Esa respuesta se guarda en la lista vacia de notas con el metodo append
# y luego se hace un for para recorrer ambas listas con len(asignatura) cuentas cuantas asignaturas existen y con el range generas una secuencia de numeros de 0 al 4 

# i toma el valor de la secuencia entonces (0,1,2,3,4)
# y accede a la posicion de ambas osea asignatura[0] notas[0]
# luego  asignatura[1] notas[1]
# luego  asignatura[2] notas[2]
# luego  asignatura[3] notas[3] y asi sucesivamente dando el print de cada una de las respuestas.

