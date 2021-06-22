#Tarea:
# Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla. 
import os

list = []

nameOne = input("Ingrese el primer nombre: ")
list.append(nameOne)
nameTwo = input("ingrese el segundo nombre: ")
list.append(nameTwo)
nameThree = input("ingrese el tercer nombre: ")
list.append(nameThree)

#for i in list:
   # print(f"nombre: {i}")
os.system('cls')
if len(nameOne) > len(nameTwo) and len(nameOne) > len(nameThree):
    print(f"el nombre {nameOne} tiene mayor cantidad de caracteres")
elif len(nameTwo) > len(nameOne) and len(nameTwo) > len(nameThree):
    print(f"el nombre {nameTwo} tiene mayor cantidad de caracteres")
else:
    print(f"el nombre {nameThree} tiene mayor cantidad de caracteres")

#otra forma!
#nombre =[]
#for i in range(3):
    #valor = input("ingrese su nombre:")
    #nombre.append(valor)
#mas_caracteres = nombre[0]
#for i in range(3):
    #if len(nombre[i])> len(mas_caracteres):
        #mas_caracteres = nombre[i]
#print(f"el nombre con más caracteres es : {mas_caracteres}")
#PROFEEEEEE
#import os

#os.system('cls')

#nombre=[]

# i toma los valores 0,1,2

#for i in range(3):

    #valor = input("Ingrese nombre:")

    #nombre.append(valor)

#mas_caracteres=nombre[0]

#for i in range(3):

    #if len(nombre[i])>len(mas_caracteres):

       # mas_caracteres=nombre[i]

#print(f"El nombre con más caracteres es:{mas_caracteres}")