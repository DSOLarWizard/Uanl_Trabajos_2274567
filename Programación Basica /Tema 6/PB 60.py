#problema 60 - crear la funcion promedio usando la funcion sumatoria

def promedio(lista):
    x = sum(lista)/len(lista)
    return x

print("bienvenido al calculador de promedio")
while True:
    num = 1
    lista1 = []

    print("priero hay que ingresar todos los valores a promediar, ingrese valores individuales y para terminar elija 0")
    while num != 0:
        num = float(input(":"))
        lista1.append(num)
        
    print("El promedio de tus valores es:",promedio(lista1))

    det = int(input("para finalizar elija 1, para continuar elija cualquier otro valor"))
    if det == 1:
        break

print("A bueno se cuida mi loco")    
