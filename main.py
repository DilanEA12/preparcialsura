#Llamando las funciones

import random

from funcionUno import ingresar_usuario
from funcionDos import crear_listado
from funcionTres import clasificar_prenda

ingresar_usuario("dilan@gmail.com", "12345678", "dilan echavarria", 8, "bellokistan")

prenda = {
        "id" :random.randint(1,100),
        "tipo" :random.choice(["Camisa", "jean", "correa", "gorra", "buzo"]),
        "marca" :random.choice(["adidas", "nike", "jordan", "lacoste", "ardidas"]),
        "precio" :random.choice([21000, 30000, 45000, 70000]),
        "estado" :random.choice(["bueno", "optimo", "regular"])
    }

crear_listado(10, prenda)

clasificar_prenda("REGULAR")