#Se ingresan RUT de personas en una lista luego mostrar solo aquelloslos RUT con menos caracteres
#*Usar funciones. 

import os
os.system('cls')
listRut=[]

def rut():
    
    answer = "s"
    while answer != "n":
        ingRut = input("ingrese rut: ")
        if len(ingRut) ==8 or len(ingRut) <= 9:
            listRut.append(ingRut)

        else:
            print("rut invalido, ingrese de nuevo")
        answer = input("Desea agregar otro rut? s/n")


def SmallRut():
    smallrut=[]
    
    for i in range(len(listRut)):
        if len(listRut[i]) < 9:
            smallrut.append(listRut[i])
            
    for i in smallrut:

        print(f"los rut más pequeño son: ")
        print(f"-{i}")


rut()
SmallRut()