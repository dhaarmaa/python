import os
os.system('cls')
#from typing import List 
list = []
answer = "si"

while answer!="no":
    name= input("ingrese un nombre: ")
    list.append(name)
    answer = input("Desea agregar otro nombre? si/no: ").lower()

list.sort()
for i in range(len(list)):
    print(f"nombre es : {list[i]}")

lessCharacters = list[0]

for i in range(len(list)):
    if len(list) < len(lessCharacters):
        lessCharacters = list[i]

list.remove(lessCharacters)
print("***********************")
for name in list:
    print(name)

