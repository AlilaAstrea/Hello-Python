'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
paso = [] # lista vacia

for sujeto in asignaturas:
    puntaje = float(input("¿Qué nota has sacado en " + sujeto + " ?"))
    if puntaje >= 5:
        paso.append(sujeto)

for sujeto in paso:
    asignaturas.remove(sujeto)
print("Tienes que repetir " + str(asignaturas))


# ----------------------------------------------------------------------------------------

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))

# ----------------------------------------------------------------------------------------

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Recorremos la lista y pedimos las notas, filtrando solo las asignaturas reprobadas
reprobadas = [asignatura for asignatura in asignaturas if float(input(f"¿Qué nota has sacado en {asignatura}? ")) < 5]

print("Tienes que repetir " + str(reprobadas))