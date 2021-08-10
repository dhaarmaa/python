def Ingresar_nombres():

    respuesta = "s"

    while respuesta =="s":

        nombre = input("Ingrese nombre:")
        personas.append(nombre)
        respuesta = input("Ingresa otro nombre s/n?").lower()


def Mostrar_nombres():

    print("--- Lista de Nombres ---")
    for i in range(len(personas)):
        print(f"* {personas[i]}")

#agregar funcion para eliminar un nombre
def Elimanar_nombre():
    print("eliminar nombre")
    nombre = input("ingrese el nombre que quiere eliminar")
    personas.remove(nombre)

#agregar funcion que me ordene la lista
def Ordenar_lista():
    personas.sort()
    print("lista ordenada")
#bloque de inicio

import os

os.system('cls')

personas = []

Ingresar_nombres()
Mostrar_nombres()
Elimanar_nombre()
Ordenar_lista()


print("Fin del programa...")