#problema 59 - crear función que calcule la sumatoria

def sumatoria(n, ec):
    suma = 0
    for i in range(1,n+1):
        suma += ec(i)
    return suma

print("bienvenido a la calculeadora de sumatorias, para que no te rompas la cabeza por lentejo xdxdxd ntc")

print("ingrese el numero de terminos")
N = int(input(":"))
print("ingrese los terminos a,b y c para una ecuación de la forma cuadratica")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

f = lambda i: a*i**2 + b*i + c

print("el resultado de la sumatoria es",sumatoria(N,f))
print("Que tenga buen día")
