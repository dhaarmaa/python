import os

os.system('cls')

cadena = "hola mundo"

# len cuenta los caracteres
largo = len(cadena)
print(f"{cadena} tiene {largo} caracteres")

# extraer una subcadena de la cadena
subcadena=cadena[0:4]
print(f"subcadena es:{subcadena}")

subcadena=cadena[:6]
print(f"ahora subcadena es:{subcadena}")

subcadena=cadena[6:]
print(f"subcadena ahora es:{subcadena}")

#buscar una subcadena o caracter 
indice = cadena.find("m")
print(f"m se encuentra en el indice {indice}")

#a mayúsculas

mayusculas = cadena.upper()
print(f"En mayúsculas es:{mayusculas}")

minusculas = cadena.lower()
print(f"En minúsculas es:{minusculas}")

h_mayusculas= cadena[0:1].upper()
print(f"En mayúculas el primer caracter es:{h_mayusculas}")