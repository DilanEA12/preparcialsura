#Necesito crear un programa en python que me permita registrar 5 prendas de vestir

'''producto_uno = input("Digite el nombre del producto: ")
producto_dos = input("Digite el nombre del producto: ")
producto_tres = input("Digite el nombre del producto: ")
producto_cuatro = input("Digite el nombre del producto: ")
producto_cinco = input("Digite el nombre del producto: ")

print(f"El nombre de los productos son {producto_uno}, {producto_dos}, {producto_tres}, {producto_cuatro}, {producto_cinco}")

marca_uno=input("Digite la marca: ")
marca_dos=input("Digite la marca: ")
marca_tres=input("Digite la marca: ")

print(f"Las marcas son: {marca_uno}, {marca_dos}, {marca_tres}")'''

#Necesito crear 1000000 prendas
#id
#tipo
#marca
#precio
#estado

import random

prendas = []
for i in range (10000000000000):
    prenda = {
        "id" :random.randint(1,100),
        "tipo" :random.choice(["Camisa", "jean", "correa", "gorra", "buzo"]),
        "marca" :random.choice(["adidas", "nike", "jordan", "lacoste", "ardidas"]),
        "precio" :random.choice([21000, 30000, 45000, 70000]),
        "estado" :random.choice(["bueno", "optimo", "regular"])
    }
    prendas.append(prenda)
print(prendas)
    








