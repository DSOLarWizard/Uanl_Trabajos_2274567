#problema 63 - funcion que eleve los elementos de una lista al cuadrado

def squr_lista(a):
    b = []
    for i in a:
        x = i**2
        b.append(x)
    return b

print("Prueba para listas al ^2: ingrese valores que quiera elevar al cuadrado y luego elija 1 parafinalizar")
lista = []
while True:
    Ter = float(input(":"))
    if Ter != 1:
        lista.append(Ter)
    else:
        break
print("Los cuadrados de los numeros",lista ,"son",squr_lista(lista))
print("Finn")
