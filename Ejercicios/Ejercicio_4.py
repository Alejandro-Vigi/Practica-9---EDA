#Escribir una función que reciba una lista y sume todos los números en la lista.

#Creacion de la lista
numeros = [1,2,3,4,5,6]

#Creacion de la funcion sumaLista la cual devolvera la suma de la lista.
def sumaLista(numeros):
    aux = 0
    #Ciclo que sirve para usar los elementos de la lista.
    for i in numeros :
        aux += i
    return aux

#Impresion en pantalla haciendo uso de la funcion y de la lista.
print(f"la suma de la lista es: {sumaLista(numeros)}")