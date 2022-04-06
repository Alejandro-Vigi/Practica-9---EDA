"""
Este programa ilustra el uso de cadenas en python
"""

#Asignado de valores iniciales

str1 = "Hola"
str2 = "mundo"
print(str1)
print(str2)

concat_cadenas = str1 + str2 #concatenacion de cadenas
print(concat_cadenas)
concat2 = str2 + str1
print(concat2)

#La funcion str convierte cualquier tipo de dato en cadena
str3 = concat_cadenas + ' ' + str(3)
print (str3)

PI = 3.1416
str4 = str3 + 'Pi = ' + str(PI) 
print(str4)

"""
La funcion format sirve para concatenar cadenas
"""

str5 = "{} {} {} {}".format(str1, str2, str3, str4)
print(str5)

str6 = "Cambiando el orden {1} {2} {0}".format(str1, str2, 3)
print(str6)