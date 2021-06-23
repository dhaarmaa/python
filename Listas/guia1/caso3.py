import os 
os.system('cls')

list=[]
answer = "s"
while answer!= "n":
    name = input("ingrese un nombre: ")
    list.append(name)
    answer = input("Desea agregar otro nombre(s/n): ").lower()


found = False
quest = input("ingrese el nombre que busca : ")
for i in range(len(list)):
    if list[i] == quest:
        found = True
        location = i
        break
if found:
    print(f"el nombre {quest} esta en el indice {location}")
else:
    print("nombre no encontrado")
