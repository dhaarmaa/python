import os

os.system('cls')

lista_nombres=[]

respuesta="si"

while respuesta!="no":

    nombre = input("Ingrese nombre:")

    lista_nombres.append(nombre)

    respuesta=input("¿Desea ingresar otro nombre si/no?").lower()

lista_nombres.sort()

#muestra la lista ordenada

for i in range(len(lista_nombres)):

    print(f"Nombre es:{lista_nombres[i]}")

# busca el nombre con menos caracteres

menos_caracteres=lista_nombres[0]

for i in range(len(lista_nombres)):

    if len(lista_nombres[i])<len(menos_caracteres):

        menos_caracteres=lista_nombres[i] #guarda el nombre con menos caracteres

# fuera del for borramos por el nombre 

lista_nombres.remove(menos_caracteres)

print("------------------------------")

#otra manera de mostrar la lista

for nombre in lista_nombres:

    print(nombre)