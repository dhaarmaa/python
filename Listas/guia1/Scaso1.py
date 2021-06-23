#otra forma!
nombre =[]
for i in range(3):
    valor = input("ingrese su nombre:")
    nombre.append(valor)
mas_caracteres = nombre[0]
for i in range(3):
    if len(nombre[i])> len(mas_caracteres):
        mas_caracteres = nombre[i]
print(f"el nombre con más caracteres es : {mas_caracteres}")
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