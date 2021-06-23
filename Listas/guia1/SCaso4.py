import os

lista_producto= []
lista_precio = []
ejecutar= True
while ejecutar:
    try:
        os.system('cls')
        print("== Menú de Opciones==")
        print("1.Ingresar productos\n2.Listar los productos y total\n3.Modificar precio de un producto\n4.Eliminar producto\n5.Salir")
        opcion=int(input("Ingrese opción: "))
        while opcion<1 or opcion>5:
            opcion=int(input("Opción incorrecta... Ingrese opción: "))
        if opcion==1:
            print("-- Ingreso de Producto--")
            activar=True
            while activar:
                producto= input("Ingrese producto: ")
                precio= int(input("Ingrese precio: $"))
                lista_producto.append(producto)
                lista_precio.append(precio)
                respuesta = input("¿Desea Ingresar otro producto s/n?").lower()
                while respuesta!="s" and respuesta!="n":
                    respuesta = input("Respuesta incorrecta...¿Desea ingresar otro producto s/n?").lower()
                if respuesta=="s":
                    activar= True
                else:
                    activar= False
        elif opcion==2:
            if len(lista_producto)>0:
                print("-- Listado de Productos--")
                suma= 0
                for indice in range(len(lista_producto)):
                    print(f"* {lista_producto[indice]}... ${lista_precio[indice]}")
                    suma += lista_precio[indice]
                print(f"Total es: ${suma}")
            else:
                print("Debe ingresar productos para poder listar...")
        elif opcion==3:
            print("-- Modificación de precios --")
            producto_buscado = input("Ingrese producto a buscar:")
            encontrado = False
            for indice in range(len(lista_producto)):
                if lista_producto[indice]==producto_buscado:
                    encontrado= True
                    ubicacion= indice
                    break
            if encontrado:
                nuevo_precio = int(input("Ingrese nuevo precio: $"))
                lista_precio[ubicacion]= nuevo_precio
                print("Listo... ¡Modificacion éxitosa!")
            else:
                print("No se encontro ningun producto con ese nombre...")
        elif opcion==4:
            print("-- Eliminar un Producto --")
            producto_buscado = input("Ingrese producto a eliminar:")
            encontrado = False
            for indice in range(len(lista_producto)):
                if lista_producto[indice]==producto_buscado:
                    encontrado= True
                    ubicacion= indice
                    break
            if encontrado:
                lista_producto.pop(ubicacion)
                lista_precio.pop(ubicacion)
                print("Producto ha sido borrado de la lista...")
            else:
                print("No existe producto con ese nombre para borrar...")
        elif opcion==5:
            ejecutar=False
            print("Fin del programa...")
        pausa=input("Presione Enter para continuar...")
    except:
        print("Ocurrió un error al ingresar...")
        pausa = input("Presione Enter para continuar...")