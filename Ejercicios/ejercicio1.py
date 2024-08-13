# Tema de cadenas, listas y bucles #

'''
Nuestros robots siempre están trabajando para sus habilidades linguisticas. Para esta misión, investigan el alfabeto latino y sus aplicaciones.

El alfabeto contiene letras vocales y consonantes.
Vocales : A E I O U
Consonantes : B C D F G H J K L M N P Q R S T V W X Y Z

Suponga que se le da un bloque de texto con diferentes palabras. Estas palabras están separadas por un espacio en blanco o un punto. No habrán dos o más espacios en blanco seguidos o combinaciones d espacios en blanco y puntos. No habrán vocales con tildes en el texto. Pueden haber números en el texto pero no se consideran palabras en esta misión ( una mezcla de letras y digitos no es una palabra tampoco)

Usted debe contar el número de palabras que tienen la misma cantidad de vocales y consonantes. Las mayúsculas y minúsculas no son significativas para esta misión.

Desarolle un programa en Python que pida un bloque de texto por teclado y muestre por pantalla la cantidad de palabras que cumplen con la descripción anterior. Por ejemplo:


Usuario ingresa por teclado          | Programa muestra

Mi nombre eS :                          2 

Hola mundo :                            1

H0la mundo :                            0

Algunas Palabras pArA contar en un 
programa con algo de Python :           5 

Perro.gato.raton.pajaro.Humano. :       3
'''


# Debe tener la misma cantidad de vocales y consonantes #

# Definir las variables vocales y consonantes

vocales = "AEIOU"
consonantes = "BCDFGHJKLMNPQRSTVWXYZ"

# Ingresara palabras
texto = input("Ingrese un texto: ")

#Convertimos lo que se ingresa en mayusculas ya que las comparaciones son están en mayusculas ( vocales y consonantes )
textomayus = texto.upper()

# Comparativa ya que se pide que el bloque de texto sea en puntos o con espacios
if "." in textomayus:  
    listapalabra = textomayus.split(".")
else:
    listapalabra = textomayus.split()

# 'Usted debe contar el número de palabras que tienen la misma cantidad de vocales y consonantes'


# El método devuelve True si todos los caracteres son letras del alfabeto (a-z).
#  .isalpha()

cantidad = 0
for palabra in listapalabra:
    num_vocal = 0 # dejando las variables acá se inicializan para no iterarse
    num_conso = 0
    if palabra.isalpha(): # Con esto si la palabra tiene un digito no contará
        for caracter in palabra:
            if caracter in vocales:
                num_vocal+=1
            elif caracter in consonantes:
                num_conso+=1
        print(f"Vocales : {num_vocal}, Consonantes : {num_conso}")
    # Con esto verificamos si el numero de vocales y consonantes son iguales
        if num_conso == num_vocal:
            cantidad +=1 
print(cantidad)



print(listapalabra) # ['HOLA', 'MUNDO']
                    # ['HOLA.MUNDO'] # Ahora ['HOLA', 'MUNDO']
