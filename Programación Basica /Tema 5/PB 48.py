#Problema 48

nombres = []
barcode = []
existencia = []

x = 1

y = 0

nom = str
bar = int
exist = int

print("bienvenido al organizador de productos")

while x == 1 or x == 2:
    x = int(input("para añadr productos elija 1, para ver productos ellija 2, para cerrar el programa, elija cualquier otro numero"))

    if x == 1:
        nom = str(input("Ingrese el nombre del producto:"))
        exist = int(input("ingrese la cantidad en existencias:"))

        nombres.append(nom)
        existencia.append(exist)
        bar = len(nombres)
        barcode.append(bar)
        
    elif x == 2:
        y = int(input("introdusca el indice del prooducto:"))
        y = y - 1

        print("El producto:",nombres[y],"tiene",existencia[y],"piezas en existencia y posee el codigo",barcode[y])

print("Que tenga buen día")
        
