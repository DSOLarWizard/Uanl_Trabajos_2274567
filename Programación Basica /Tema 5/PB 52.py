#problema 52

productos = ["Masetas","Botiquines","Limpia piscinas","Guantes de jardinería","Semillas Raras"]
precios = [2500.0,2000.0,1000.0,200.0,10000.0]
ventas = [3,4,2,1,9]
ingreso = []

for x in precios:
    y = precios.index(x)
    plata = precios[y]*ventas[y]
    ingreso.append(plata)

print("Producto/Precio/Volumen de ventas/Ingresos\n")

for x in precios:
    y = precios.index(x)
    print(productos[y],"/ $",precios[y],"/",ventas[y],"/ $",ingreso[y])
