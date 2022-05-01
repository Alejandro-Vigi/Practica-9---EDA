#Definir una función que reciba un caracter y devuelva Verdadero si es vocal y falso en caso contrario.

"""Creacion de la funcion vocal la cual verifica si el caracter ingresado es una vocal mediante condicionales
   ya sea en mayusculas o minusculas, devolviendo un booleano."""
def vocal(letra):
    if letra in ('a','e','i','o','u','A','E','I','O','U'):
        return 'True'
    else:
        return 'False'

#Ingreso de la cadena mediante teclado.
caracter = input("Ingrese algun caracter: ")

#Impresion del booleano.
print(vocal(caracter))