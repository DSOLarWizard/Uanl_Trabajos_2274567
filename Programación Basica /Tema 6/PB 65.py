#problema 65 - #de factorial

def factorial(a):
    b = a - 1
    while b > 1:
        a *= b
        b -= 1
    return a

print("bienvenido a la maquina factorial!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("ingrese numeros para ver su factorial o 0 para salir")
n = 0 
while True:
    x = int(input(":"))
    if x !=0:
        print("el factorial de",x,"es",factorial(x))
        n += 1
    else:
        break
print("se calculo el factorial de",n,"numeros")
print("Si no te vuelvo a ver, buenos días, buenas tardes, y buenas noches")
