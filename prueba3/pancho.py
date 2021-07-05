import os

lista_pizza= []
lista_precio = []
ejecutar= True
while ejecutar:
    try:
        os.system('cls')
        print("== Hola bienvenidos a pizza duoc==")
        print("1.Opciones de pizza\n2.Pagar\n3.Anular pedido\n4.Salir")
        opcion=int(input("Ingrese opción:"))
        while opcion<1 or opcion>3:
          opcion=int(input("Opción incorrecta... Ingrese opción:"))
        if opcion==1:
            print("Opciones de pizza")
            print("1-Tradicional : $12000")
            print("2-Peperonni : $14000")
            print("3- Todas las carnes : $16000")
            answer = "s"
            while answer !="n":
                pizza = int(input("Ingrese su opción"))
                if pizza == 1:
                    lista_pizza.append("Tradicional")
                    lista_precio.append(12000)
                elif pizza== 2:
                    lista_pizza.append("Peperonni")
                    lista_precio.append(14000)
                elif pizza==3:
                    lista_pizza.append("Todas las carnes")
                    lista_precio.append(16000)
                else:
                    print("Opción incorrecta")
                answer =input("Desea ingresar otro producto: s/n").lower()
        elif opcion ==2:
            subtotalcompra = 0
            print("Pedido y total")
            if len(lista_pizza) < 1:
                print("No tienes productos ingresados...")
            else:
                print("Tipo de cliente:")
                print("1- Estudiante diurno")
                print("2- Otro")
                tipo_usuario = int(input("Ingrese opción:"))
                if tipo_usuario ==1:
                    for i in lista_precio:
                        subtotalcompra+= i
                        calcular = (subtotalcompra*12)/100
                        total =subtotalcompra - calcular
                elif tipo_usuario ==2:
                    for i in lista_precio:
                        subtotalcompra += i
                        total = subtotalcompra
                else:
                    print("Ingrese una opción valida....")
                print("--- Pizza DUOC---")
                for i in lista_pizza:
                    print(f"- {i}")
                print("------------------------")
                print(f"subtotalcompra : ${subtotalcompra}")
                print(f"total: - ${total}")
                print("------------------------")
            
        elif opcion ==3:
            print("anular")
        elif opcion ==4:
            ejecutar:False
            print("fin del programa")
    except:
        print("Ingrese una opcion correcta...")