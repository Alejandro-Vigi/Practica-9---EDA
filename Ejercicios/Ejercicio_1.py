#Definir una función que tome dos números y devuelva el mayor de ellos.

#Creacion de la funcion mayorQue la cual imprime las 3 posibilidades.
def mayorQue(n1, n2):
    #Condicionales con operadores verificando los datos para validar alguna de las opciones.
    if n1 < n2:
        print(f"El mayor es {n2}")
    elif n1 > n2:
        print(f"El mayor es {n1}")
    else :
        print(f"{n1} y {n2} Son iguales")

#Ingreso de datos mediante teclado.
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

#Uso de la funcion.
mayorQue(n1, n2)