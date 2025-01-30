# TIPOS DE DATOS

#------------
# TEXTO:
#------------

# - str (cadena de caracteres)
texto = "Hola mundo"

#------------
# NUMERICOS:
#------------

# - int (enetro)
numero_entero = 10

# - float (flotante)
numero_flotante = 3.14

# - complex (complejo)
numero_complejo = 2 + 3j

#------------
# SECUENCIA:
#------------

# - list(lista) [coleccion ordenada y mutable]
lista = [1,2,3,4]

# - tuple(tupa) [coleccion ordenada e inmutable]
tupla = (1,2,3)

# - range(rango) [secuencia inmutable de numeros]
rango = range(0, 10)

#------------
# MAPPING TYPE (MAPEO)
#------------

# - dict (diccionario) [Coleccion no ordenada de pares clave-valor]
diccionario = { 
    "nombre": "Sergie",
    "edad": 34
}

#------------
# SET TYPES (CONJUNTO)
#------------

# - set (conjunto) [Coleccion no ordenada y mutable de elementos UNICOS (no permite repetir)]
conjunto = {1,2,3,4}

# - frozenset (conjunto inmutable) [Conjunto inmutable]
conjunto_inmutable = frozenset({1,2,3,4})

#------------
# BOOLEAN TYPES (BOOLEANO)
#------------

# - boolean [puede ser verdadero o falso]
booleano = True
booleano2 = False

#------------
# BINARY TYPES (BINARIO)
#------------

# - bytes [Representa una secuencia inmutable de bytes]
bytes_data = b"datos"

# - bytearray (array de datos) [Una secuencia mutable de bytes]
bytearray_data = bytearray(b"datos")

# - memoryview (vista de memoria) [Permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")

#------------
# NULL (NULO)
#------------

# - NoneType (nulo) [Representa la ausencia de valor o la no definicion]
nulo = None