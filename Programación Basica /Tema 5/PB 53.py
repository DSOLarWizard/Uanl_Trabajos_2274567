#problema 53

datos = []

print("Captador y ordenador de datos, para cerrar elija como dato 'fin'")

while True:
    x = input("dato:")
    if x != "fin":
        datos.append(x)
    else:
        break
datos.sort()

print("la lista ordenada es:", datos)
