#Problema 49

nombres = []
barcode = []
existencia = []
inventario = {}

y = 0

nom = str
bar = int
exist = int

print("bienvenido al organizador de productos")

while True:
    x = int(input("para añadr productos elija 1, para ver productos elija 2,para ver el inventario completo elija 3, para cerrar el programa, elija cualquier otro numero"))

    if x == 1:
        nom = str(input("Ingrese el nombre del producto:"))
        exist = int(input("ingrese la cantidad en existencias:"))

        nombres.append(nom)
        existencia.append(exist)
        bar = len(nombres)
        barcode.append(bar)
        
        inventario[nom] = exist
        
    elif x == 2:
        y = int(input("introdusca el indice del prooducto:"))
        y = y - 1

        print("El producto:",nombres[y],"tiene",existencia[y],"piezas en existencia y posee el codigo",barcode[y])

    elif x == 3:
        print("el inventario sería:", inventario)
        
    else:
        break

print("Que tenga buen día")
        
