#Problema 50

nombres = []
barcode = []
existencia = []
inventario = {}

y = 0

nom = str
bar = int
exist = int

print("Bienvenido al organizador de productos 4ta trans del anticristo 2007")

print("Para añadr productos elija 1, para ver productos(por indice elija 2, por clave elija, 3),para ver el inventario completo elija 4, para cerrar el programa, elija cualquier otro numero")

while True:

    x = int(input("Elija una acción:"))

    if x == 1:
        nom = str(input("Ingrese el nombre del producto:"))
        exist = int(input("Ingrese la cantidad en existencias:"))

        nombres.append(nom)
        existencia.append(exist)
        bar = len(nombres)
        barcode.append(bar)
        
        inventario[nom] = exist
        
    elif x == 2:
        y = int(input("Introdusca el indice del prooducto:"))
        y = y - 1

        print("El producto:",nombres[y],"tiene",existencia[y],"piezas en existencia y posee el codigo",barcode[y])

    elif x == 4:
        print("El inventario sería:", inventario)

    elif x == 3:
        z = input("Introdusca la clave del producto:")
        print("El producto",z,"tiene",inventario[z],"existencias")
        
    else:
        break

print("Que tenga buen día")
        
