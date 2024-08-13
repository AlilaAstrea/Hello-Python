# Ejercicio Palíndromo

'''
Implemente la función buscar_palindromos(mensaje) que recibe un mensaje y retorna una lista con todas las palabras (de 2 o más letras) del mensaje que son palíndromos. Asuma que todas las palabras están en minúsculas y no existen signos de puntuación.

Recuerde que un palíndromo es una cadena que se lee igual de izquierda a derecha o de derecha a izquierda. Por ejemplo : madam, ana, somos, reconocer, anilina.

Ejemplo de entrada:
mensaje = "ana y yo somos amigos y trabajamos en la torre del radar"

Ejemplo de salida:
['ana', 'somos', 'radar']

'''

# Con slicing podemos obtener una porcion de la cadena

mensaje = "ana y yo somos amigos y trabajamos en la torre del radar"
# Imprime solo ana ya que cuenta desde 0 al 3 0,1,2,3 en la palabra es 0 = a, 1=n, 2=a, 3 termina)
print(mensaje[0:3]) # ana

# Podemos agregar un tercer parametro y por defecto esta seteado en 1, si ponemos 2 da un salto de linea
print(mensaje[0:3:2]) # aa

# si dejamos vacio el primer parametro se interpreta como que iniciamos desde el primer indice es decir (indice 0)
print(mensaje[:3:2]) # aa

# Al hacer lo mismo en el segundo parametro nos indica que llegaremos hasta el ultimo indice ( entonces salta de 2 en 2 imprimiendo cada letra hasta el final)
print(mensaje[::2]) # aayy oo mgsytaaao nl or e aa

# La cadena anterior da saltos de izquierda a derecha y si ponemos -1 obtendremos la cadena de forma reversa
print(mensaje[::-1]) # radar led errot al ne somajabart y sogima somos oy y ana

# De esta forma tendremos la solucion del palindromo de una cadena de texto ya que interpreta el mensaje al revez 


def buscar_palindromos(mensaje):
    palabras = mensaje.split(" ")
    palindromos = [] # Definimos una lista vacia
    for palabra in palabras: # recorremos las palabras
        palindromo= palabra[::-1] # palindromo es la palabra con la condicion del palindromo ( osea lo recorre al revez)
        if palabra == palindromo and len(palabra) >=2: # verificamos si la palabra es igual a su reverso entonces agregamos la palabra al listado de palindromos
            palindromos.append(palabra) # ['ana', 'y', 'somos', 'y', 'radar'] # Agregamos el len(palabra) para que no cuente las letras solas como 'y'
    

    print(palindromos)


buscar_palindromos(mensaje)  