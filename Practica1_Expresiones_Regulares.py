#Nombre:Carballo Pérez Isaac
#Fecha: 03/03/19
#Escribir un programa que determine si una placa es o no de un automovil privado de la CDMX
import re
print("**Programa para validar placas de carro en la CDMX**")
print("Recuerde que las placas deben de cumplir: "
      "\n-El primer caracter debe ser una letra"
      "\n-Los siguientes 2 caracteres deben ser digitos"
      "\n-El cuarto caracter debe ser un guion"
      "\n-Finalmente los ultimos 3 carcateres deben ser letras")
print("\nRecordar que las letras O,Q,Ñ,I no son letras validas y los digitos van del 0 al 9")

print("\nSi desea salir del programa ingrese un -1")

carros=[]

while True:
    placa= input("\nIngrese una placa de carro: ")
    entrada="^[ABCDEFHJKLMNPRSTUVWXYZ][0-9]{2}-[ABCDEFHJKLMNPRSTUVWXYZ]{3}$"
    encontrado = re.search(entrada, placa)

    if encontrado is not None:
        print("La placa es una placa valida para un automovil particular en la CDMX")
        carros.append(placa)
    else:
        print("La placa NO es valida para un automovil particular en la CDMX")
    if placa=="-1":
        #print(re.findall(entrada, placa)) #re.findall() Devuelve una lista con las coincidencias
        print("La lista de carros que pertenecen a la CDMX es:",carros)
        break