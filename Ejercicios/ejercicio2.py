
'''
Tema 1 
CuidaVehiculo ha lanzado una aplicación para llevar un control sobre mantenimiento de tu vehiculo.
Para esto, tienen un diccionario de mantenimientos preventivos y correctivos recomendados para cada parte del carro de acuerdo al numero de dias y kilometros
'''

mantenimiento = {
    'preventivo': [('llantas', 60, 4500),
                   ('bujias', 45, 3000)],
    'correctivo': [('llantas', 90, 6000),
                   ('zapatas', 120, 10000)]
}

'''
Además, posee un historial por vehiculo en donde se registra el numero de dias y el kilometraje que han pasado desde el ultimo mantenimiento
'''
historial = {
    'GEC-2411': {
        'propietario': 'Eduardo Cueva',
        'registro': [('llantas', 70, 32500),
                     ('zapatas', 180, 500)]
    },
    'GAA-0321': {
        'propietario': 'Andrea Martinez',
        'registro': [('bujias', 40, 500),
                     ('zapatas', 180, 500)]
    }
}

'''
La funcion mantenimientos(strPlaca, dictHistorial, dictMantenimiento) que recibe la placa, el diccionario con el historial por vehiculo y el diccionario de mantenimientos. Esta funcion devolvera una lsita de tuplas. Cada tupla tendra el nombre de la parte del carro y el tipo de mantenimiento a realizar ('preventivo','correctivo' o 'nada') para dicha placa.

Considere que sobre cada parte del carro solo se puede realizar un tipo de mantenimiento, preventivo o correctivo, de acuerdo a si supera el numero de dias. En caso de que el numero de dias supere el establecido para ambos tipos de mantnimiento, se debera preferir el mantenimiento correctivo.
'''


def mantenimientos(strPlaca, dictHistorial, dictMantenimiento):
    resultado = {}
    registro = dictHistorial.get(strPlaca).get("registro")
    preventivo = dictMantenimiento.get("preventivo")
    correctivo = dictMantenimiento.get("correctivo")

    for re in registro:
        parte_carro = re[0]  # primer elemento de la tupla
        dias = re[1]
        resultado[parte_carro] = "nada"

        for prev in preventivo:
            if parte_carro == prev[0]:
                if dias > prev[1]:
                    resultado[parte_carro] = "preventivo"

        for cor in correctivo:
            if parte_carro == cor[0]:
                if dias > cor[1]:
                    resultado[parte_carro] = "correctivo"
    resultado = list(resultado.items())
    return resultado


print(mantenimientos("GEC-2411", historial, mantenimiento))


'''
Item 2
La función semaforo(strPlaca, dictHistorial, dictMantenimiento) que recibe la placa, el diccionario con el historial por vehiculo y diccionario de mantenimientos. Esta funcion devuelve un diccionario cuyas claves son "amarillo", "verde", "rojo". Los valores corresponden a listas de partes para esa placa que necesitan un mantenimiento preventivo (en la clave "amarillo"), correctivo (en la clave "rojo") o ningun mantenimiento ( en la clave "verde")

'''


def semaforo(strPlaca, dictHistorial, dictMantenimiento):
    resultado = {}
    lista_prev = []
    lista_cor = []
    nada = []

    mant = mantenimientos(strPlaca, dictHistorial, dictMantenimiento)

    for m in mant:
        if m[1] == "preventivo":
            lista_prev.append(m[0])
            resultado["amarillo"] = lista_prev
        elif m[1] == "correctivo":
            lista_cor.append(m[0])
            resultado["rojo"] = lista_cor
        else:
            nada.append(m[0])
            resultado["verde"] = nada

    return resultado


print(semaforo("GEC-2411", historial, mantenimiento))

'''
La funcion recomendar(dictHistorial, dictMantenimiento, strParte,strTipoMantenimiento) que recibe el diccionario con el historial por vehiculo, diccionario de mantenimientos, el nombre de una parte, y el tipo de mantenimiento ("preventivo" o "correctivo"). La funcion debera retornar una lista con todas las placas de los vehiculos que ya necesitan mantenimiento de strTipoMantenimiento en strParte

'''


def recomendar(dictHistorial, dictMantenimiento, strParte, strTipoMantenimiento):
    resultado = []
    placas = dictHistorial.keys()
    for placa in placas:
        mant = mantenimientos(placa, dictHistorial, dictMantenimiento)
        for m in mant:
            if m[0] == strParte and m[1] == strTipoMantenimiento:
                resultado.append(placa)

    return resultado


print(recomendar(historial, mantenimiento, "llantas", "preventivo"))
