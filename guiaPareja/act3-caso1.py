# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
#a. User1: pedro Contraseña1: 1234
#b. User2: angel Contraseña2: a4s1
import os
os.system('cls')

user = input("ingrese su nombre de usuario: ")
password = input("ingrese su contraseña: ")

#userOne = "pedro"
if user== "pedro" and password == "1234":
    print("usuario valido")
elif user == "angel" and password == "a4s1":
    print("usuario valido")
else:
    print("usuario invalido")
