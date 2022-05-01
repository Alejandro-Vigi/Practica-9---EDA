#Escribir una función que devuelva la cadena inversa de una cadena dada.

#Creacion de la funcion inversa la cual invertira una cadena dada por el usuario.
def inversa(s): 
  str = ""
  #Ciclo que sirve para invertir caracter por caracter en la cadena dada.
  for letra in s: 
    str = letra + str
  return str

#Ingreso de la cadena desde teclado.
s = input(str("Introduce la cadena: "))

#Impresion de pantalla de la lista original.
print("La cadena original es: ")
print(s)

#Impresion de pantalla de la lista una vez ya invertida efectuando la funcion.
print("La cadena inversa es: ")
print(inversa(s))

