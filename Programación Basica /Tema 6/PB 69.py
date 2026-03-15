#Problema 69
def validarCorreo(dirreccion):
    x = 0
    x += dirreccion.count("@")
    x += dirreccion.count(".edu")
    x += dirreccion.count(".com")
    x += dirreccion.count(".es")
    x += dirreccion.count(".org")
    x += dirreccion.count(".mx")
    if x == 2:
        return "si"
    else:
        return "no"

print("Validación de correo, ingrese su Email")
mail = str(input(":"))

if validarCorreo(mail) == "si":
    print("correo valido")
else:
    print("correo invalido")
    
    
