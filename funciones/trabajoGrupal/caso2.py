#Dadas dos listas pobladas con marcas de vehículos, se pide generar una tercera sólo con los elementos que estén repetidos en ellas. Considerar que la nueva lista no contenga elementos duplicados. *Usar funciones.
import os 
os.system('cls')
listOne = ["Mazda", "Audi", "Chevrolet", "Volvo", "Jeep", "Mercedes-Benz", "Ford", "Lexus", "jaguar", "infiniti", "Audi", "Porsche", "maserati" , "land Rover" , "Ferrari"]
listTwo = ["Audi", "Audi", "Chery", "Dodge", "Ford", "Ferrari", "BMW", "Bugatti", "Mercedez", "Nissan", "Toyota", "Porsche",  "Honda", "Chevrolet", "Hyundai", "Volkswagen", "Kia", "Mini", "Tesla"]

def duplicateMarks():
    listThree = []
    for i in range(len(listOne)):
         for j in range(len(listTwo)):
             if i !=j:
                 if listOne[i] == listTwo[j] and listOne[i] not in listThree:
                     listThree.append(listOne[i])
    print(listThree)

duplicateMarks()

    
        