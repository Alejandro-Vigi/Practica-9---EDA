#Definir una lista con un conjunto de nombres, imprimir la cantidad de nombres que comienzan con “a”

#Creacion de la lista.
nombres = []

#Ingreso de la cantidad de nombres a introducir a la lista mediante teclado.
numNombres = int(input("¿Cuantos nombres deseas ingresar a la lista?: "))

#Ciclo que permite introducir los nombres a la lista.
for x in range(0, numNombres):
    nombres.append(input("Escribe un nombre: ").capitalize())

#Ingreso de la letra a buscar mediante teclado.
letra_buscada = input("¿Que letra buscas?: ").capitalize()
cantidad = 0


#Ciclo que permite mediante condicionales calcular la cantidad de nombres en la lista que inician con 
#la letra indicada por el usuario.
for nombre in nombres:
    for letra in nombre:
        if letra == letra_buscada:
                cantidad = cantidad + 1
                break
        else:
                cantidad = cantidad
                
#Impresion en pantalla de la cantidad de nombres con dicha letra al inicio.
print("La cantidad de nombres que inician con la letra " + str(letra_buscada)  + " es: ")
print (cantidad)