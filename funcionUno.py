#Funcion para evaluar correos y contraseñas

def ingresar_usuario(correo_usuario, contraseña, nombre, edad, ciudad):
    CORREO_BD="prueba@gmail.com"
    CONTRASEÑA_BD="12345678"

    if (correo_usuario == CORREO_BD) and (contraseña_usuario == CONTRASEÑA_BD):
        return("¡Bienvenido, " + nombre_usuario + "!")
    else:
        return("Correo electrónico o contraseña incorrectos. Por favor, inténtelo de nuevo.")

