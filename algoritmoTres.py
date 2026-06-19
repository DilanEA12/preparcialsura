


estado_prenda = input("Digita el estado de la prenda: ").upper()

valor_prenda = None
if estado_prenda == "REGULAR":
    valor_prenda = 10
    print(valor_prenda)
elif estado_prenda == "BUENO":
    valor_prenda = 50
    print(valor_prenda)
elif estado_prenda == "OPTIMO":
    valor_prenda = 100   
    print(valor_prenda) 
else:
    print("valor invalido")