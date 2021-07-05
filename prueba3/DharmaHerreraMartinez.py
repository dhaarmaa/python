import os 
listPizza = []
listCost = []


ejecutar = True
while ejecutar:
    try:
        print("\t          BIENVENIDO A PIZZADUC")
        print("**********************************************************")
        print("         *               MENU                *            ")
        print("**********************************************************")
        print ("\t1 - Realizar pedido")
        print ("\t2 - Pagar")
        print ("\t3 - Anular pedido")
        print ("\t4 - Salir")

        option =int(input("Ingrese opcion: "))
        os.system('cls')
        if option ==1:
            print("\tOPCIONES DE PIZZA")
            print ("\t1 - Tradicional : $12000")
            print ("\t2 - Peperonni : $14.000")
            print ("\t3 - Todas las Carnes : $16.000")
            answer = "s"
            while answer !="n":
                pizza = int(input("Ingrese su opcion: "))
                
                if pizza == 1:
                    listPizza.append("Tradicional")
                    listCost.append(12000)
                   
                elif pizza ==2:
                    listPizza.append("Peperonni")
                    listCost.append(14000)
                elif pizza ==3:
                    listPizza.append("Todas las carnes")
                    listCost.append(16000)
                else:
                    print("opcion ingresada invalida")
                answer = input("Desea ingresar otro producto s/n: ").lower()
        elif option ==2:
            subTotal = 0
            print("\tPedido y total")
            if len(listPizza) < 1:
                print("No tiene productos ingresados...")

            else:
                print("Tipo de cliente:")
                print ("\t1 - Estudiante diurno")
                print ("\t2 - otro")
                
                for i in listCost:
                    subTotal+=i

                typeUser = int(input("Ingrese su opción: "))
                
                if typeUser ==1:
                    calculation = (subTotal*12)/100
                    total = subTotal - calculation
                    
                elif typeUser ==2:
                    total = subTotal
                    calculation = 0
                else:
                    print("Opción invalida..")

                money = int(input(f"El total es : ${subTotal}. Ingrese el dinero: "))
                if money < subTotal:
                    print("Dinero insuficiente para el pago")
                else:
                    change= money-total
                
                
                #number = [listPizza.count(item) for item in listPizza]
                    print("******PIZZA DUOC******")
                    print("--------------------------")
                    #for i in listPizza:
                        #print(f"- {i}")
                    #for i in listCost:
                        #total+= i
                    [print(listPizza.count(item), item) for item in set(listPizza)]
                    print("--------------------------")
                    print(f"Sub total : ${subTotal}")
                    print(f"Descuento :  ${calculation}")
                    print("--------------------------")
                    print(f"Total: ${total}")
                    print(f"Dinero ingresado : ${money}")
                    print(f"Vuelto: ${change}")
        elif option ==3:
            print("Anular")
            listPizza.clear()
            listCost.clear()
            print("Pedido anulado")
        elif option ==4:
            ejecutar = False
            print("\tFin del programa")
        else:
            print("Opción invalida")
        if ejecutar:
            pause = input("Presione Enter para volver al menu principal...")
    except:
        print("Ha ocurrido un error al ingresar...")

        pause = input("Presione Enter para continuar...")