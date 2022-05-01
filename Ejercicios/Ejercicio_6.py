#Hacer un programa que convierta números binarios en enteros.

#Ingreso de datos mediante teclado.
binario = input("Ingrese un numero en forma binaria: ") 

#Conversion de la variable binario a un numero entero
entero = int(str(binario),2)

#Impresion en pantalla de la variable ya convertida en entero.
print(entero)