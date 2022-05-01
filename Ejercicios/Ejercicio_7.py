#Hacer un program que defina una tupla con 10 edades de personas, imprimir la 
#cantidad de personas con edades superiores a 20.

#Creación de la tupla
tupla = [40,10,6,3,1,21,14,34,52,20]

#Creacion de la variable auxiliar para llevar acabo el conteo.
cantidad = 0

#Ciclo que permite usar los elementos de la tupla el cual contiene condicionales para llevar acabo el conteo.
for edad in tupla:
    if edad >= 20:
        cantidad = cantidad + 1
    else:
        continue
    
#Impresion en pantalla
print("La cantidad de personas con edades superiores a 20 es: ")
print(cantidad)