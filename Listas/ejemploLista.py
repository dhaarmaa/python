import os

os.system('cls')

#define una lista 

lista = []

lista.append("juana")

lista.append("pedro")

lista.append("diego")

lista.append("ana")

print(f"{lista}")

print(f"{lista[0]}")

print("---------- Nombres ----------")

for dato in lista:

    print(f"Nombre:{dato}")

lista.insert(0,"claudio")

print("---------- Nombres ----------")

for dato in lista:

    print(f"Nombre:{dato}")

#ordena la lista

lista.sort() #sort solo permite ordenar datos del mismo tipo

print("---------- Nombres Ordenados ----------")

for dato in lista:

    print(f"Nombre:{dato}")

lista.reverse()

print("---------- Nombres en reversa ----------")

for dato in lista:

    print(f"Nombre:{dato}")

lista.pop(0) #elimina el primer elemento por indice

print("---------- Dato elimminado ----------")

for dato in lista:

    print(f"Nombre:{dato}")

lista.remove('ana') #elimina por el dato ingresado

print("---------- Dato elimminado ----------")

for dato in lista:

    print(f"Nombre:{dato}")

for veces in range(0,2):

    nombre=input("Ingrese nombre:")

    lista.append(nombre)

print("---------- Nombres ----------")

for dato in lista:

    print(f"Nombre:{dato}")