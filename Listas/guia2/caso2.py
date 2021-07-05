listDescription=[]
listHours = []
listPriority =[]

answer = "s"
while answer!="n":
    description=input("ingrese la descipción de la reunion: ")
    listDescription.append(description)
    hours = input("ingrese el horario: ")
    listHours.append(hours)
    priority = input("ingrese el tipo de prioridad. alta/baja: ").lower()
    listPriority.append(priority)
        
    answer = input("desea agregar otra reunión? s/n: ").lower()
for i in range(len(listDescription)):
    
    print(f"{listPriority[i]} {listDescription[i]} {listHours[i]}")
