import os 
list = []
answer = "si"

while answer != "no":
    name= input("ingrese un nombre: ")
    list.append(name)
    answer = input("Desea agregar otro nombre? s/n: ").lower
list.sort()
for i in list:
    print(f"nombre: {i}")