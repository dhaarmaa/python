import os 
#edfonir lista
list=[]
list.append("dharma")
list.append("ali")
list.append("vale")
list.append("mati")
list.append("ricardo")
list.append("pancho")
list.append("jose")
for dato in list:
    print(f"nombre: {dato}")
print("************************")
list.insert(0, "profe claudio")
for dato in list:
    print(f"nombre: {dato}")

list.sort()
print("************************")
for dato in list:
    print(f"nombre: {dato}")
list.reverse()
print("************************")
for dato in list:
    print(f"nombre: {dato}")

list.remove("profe claudio")
print("************************")
for dato in list:
    print(f"nombre: {dato}")

list.append("javier")
print("************************")
for dato in list:
    print(f"nombre: {dato}")

list.pop(7)
print("************************")
for dato in list:
    print(f"nombre: {dato}")
print("*******************")
for i in  range(0,2):
 nomber = input("ingrese nombre")
 list.append(nomber)
 print("************************")
for dato in list:
    print(f"nombre: {dato}")
