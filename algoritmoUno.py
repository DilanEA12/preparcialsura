#Entradas del sistema
'''nombre_usuario = None
correo_usuario = None
contraseña_usuario = None
ciudad_usuario = None
edad_usuario = None'''

nombre_usuario = input("Ingrese su nombre de usuario: ")
correo_usuario = input("Ingrese su correo electrónico: ")
contraseña_usuario = input("Ingrese su contraseña: ")
ciudad_usuario = input("Ingrese su ciudad de residencia: ")
edad_usuario = int(input("Ingrese su edad: "))

CORREO_BD="prueba@gmail.com"
CONTRASEÑA_BD="12345678"

#Condicional en python
if (correo_usuario == CORREO_BD) and (contraseña_usuario == CONTRASEÑA_BD):
    print("¡Bienvenido, " + nombre_usuario + "!")
else:
    print("Correo electrónico o contraseña incorrectos. Por favor, inténtelo de nuevo.")