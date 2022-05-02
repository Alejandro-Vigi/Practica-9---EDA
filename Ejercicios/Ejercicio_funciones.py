#Ejercicio de funciones str mediante la documentacion vista en clase.

import xdrlib

str1 = "hola mundo"
print(str.capitalize(str1))
#Devuelve la cadena con la primera letra en mayusculas.

str2 = "Cadena contada" 
print(str.isdecimal(str2))
#Devuelve un booleano si todos los caracteres son decimales y hay al menos un caracter.

str3 = "41325"
print(str.isdigit(str3))
#Retorna un booleano verificando si toda la cadena es de digitos.

str4 = "cadenaenminuscula"
print(str.islower(str4))
#Retorna un booleano verificando si toda la cadena esta en minusculas.

str5 = "     "
print(str.isspace(str5))
#Retorna un booleano verificando si la cadena solo contiene espacios.

str6 = "CADENAENMAYUSCULAS"
print(str.isupper(str6))
#Retorna un booleano verificando si toda la cadena esta en mayusculas.

str7 = "Cadena convertida A MINUSCULAS"
print(str.lower(str7))
#Retorna la cadena en minusculas.

str8 = "cadena convertida a mayusculas"
print(str.upper(str8))
#Retorna la cadena en mayusculas.

str9 = "hola mundo"
print(str.title(str9))
#Convierte la cadena como tipo titulo

str10 = "CADENA Minusculas como la LETRA EN alemán ß"
print(str.casefold(str10))
#Retorna la cadena en minusculas pero de una manera mas agresiva