
cont = 0
suma = 0

while cont < 10:
    try:
        nota = float(input("Ingresa una nota del 1 al 7"))
        if nota >= 1 and nota <= 7:
            suma += nota
            cont += 1
        else:
            print("Ingrese notas validas")
    except ValueError:
        print("Ingrese valores validos")
print(f"Tu promedio de notas es igual a {suma / cont}")