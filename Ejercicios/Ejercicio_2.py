#Definir una función que calcule la longitud de una lista o una cadena dada.

#Creacion de la funcion longitud la cual contara la cantidad de caracteres y espacios retornandolos.
def longitud(frase):
    espacio = 0
    caracter = 0
    #Ciclo que permite llevar acabo el conteo de la longitud verificando mediante condicionales los espacios.
    for i in frase:
        if i == " ":
            espacio = espacio + 1
            continue
        caracter = caracter + 1
    return caracter, espacio

#Ingreso de la cadena mediante teclado.
frase = input(str("Ingresa la frase: "))

#Impresion de datos en la pantalla.
print(f"\nNumero de caracateres: {longitud(frase)[0]}\nNumero de espacios: {longitud(frase)[1]}")