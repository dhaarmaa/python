
import os 
listProducts = []
listCost = []

ejecutar = True
while ejecutar:
    try:
        print("**********************************************************")
        print("         *               MENU                *            ")
        print("**********************************************************")
        print ("\t1 - Ingresar productos")
        print ("\t2 - Listar los productos y  total")
        print ("\t3 - Modificar precio de un producto")
        print("\t4 - Eliminar un producto")
        print ("\t5 - Salir")

        option =int(input("Ingrese opcion: "))
        os.system('cls')
        if option ==1:
            print("\tIngreso de productos")
            answer = "s"
            while answer !="n":
                products = input("Ingrese su producto: ")
                listProducts.append(products)
                cost = int(input("Ingrese su valor:$ "))
                listCost.append(cost)
                answer = input("Desea ingresar otro producto: s/n").lower()
                
        elif option==2:
            total = 0
            print("\tLista de productos y total")
            if len(listProducts) < 1:
                print("No tiene productos ingresados...")
            else:
                print("PRODUCTOS:")
                for i in listProducts:
                    print(f"- {i}")
                for i in listCost:
                    total+= i
                print(f"total: ${total}")
        elif option ==3:
            print("\tModificacion de precio de un producto")
            quest = input("ingrese el producto que busca: ")
            index = listProducts.index(quest)
            newCost = int(input(f"el producto {quest} tiene un valor de ${listCost[index]}. Ingrese su nuevo valor: $"))
            listCost[index] = newCost
        elif option ==4:
            print("\tEliminacion de un producto")
            deleteProduct = input("Ingrese el producto que quiere eliminar: ")
            index = listProducts.index(deleteProduct)

            listProducts.pop(index)
            listCost.pop(index)
        elif option ==5:
            ejecutar = False
            print("\tfin del programa")
            
        else:
            print("opcion invalida")
        if ejecutar:
            pause = input("Presione Enter para volver al menu principal...")

    except:
        print("Ha ocurrido un error al ingresar...")

        pause = input("Presione Enter para continuar...")
