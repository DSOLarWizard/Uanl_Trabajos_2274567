#problema 55

lista = list()

print("para crear una lista de numeros elija 1, para crear una lista de texto elija 2")

x = int(input(":"))

print("Para ver la lista elija 1, para agregar valores a la lista elija 2,para eliminar valores elija 3,para ordenar la lista elija 4, para verificar si la un elemento se encuentra en la lista elija 5")

if x == 1:
    print("para calcular el valor maximo elija 6, para calcular e valor minimo elija 7, para sumar los elementos en la lista elija 8,y para calcular el promedio de los elementos elija 9")

print("por ultimo si desea terminar el programa elija 0")

while True:
    y = int(input("Acción:"))
    if y == 2:
        if x == 1:
            ad = float(input("ingrese el numero a añadir\n:"))
        elif x == 2:
            ad = str(input("ingrese el texto a añadir\n:"))
        lista.append(ad)

    elif y == 1:
        print(lista)

    elif y == 3:
        if x == 1:
            kill = float(input("ingrese el numero a eliminar\n:"))
        elif x == 2:
            kill = str(input("ingrese el texto a eliminar\n:"))
        lista.remove(kill)

    elif y == 4:
        acomodar = int(input("para ordenar la lista de manera directa, elija 1, para crear una nueva lista ordenada elija 2\n:"))
        if acomodar == 1:
            lista.sort()
        elif acomodar == 2:
            lista_ordenada = sorted(lista)
    elif y == 5:
        if x == 1:
            buscar = float(input("Que elemento desea buscar?\n:"))
        elif x == 2:
            buscar = str(input("Que elemento desea buscar?\n:"))
        if buscar in lista:
            print("el objeto se encuentra en la posición",lista.index(buscar))
        else:
            print("el objeto no se encuentra en la lista")
    if x == 1:
        if y == 6:
            print("el maximo de la lista es:",max(lista))
        elif y == 7:
            print("el minimo de la lista es:",min(lista))
        elif y == 8:
            print("la suma de los elementos da",sum(lista))
        elif y == 9:
            print("el promedio de los elementos da",sum(lista)/len(lista))
    if y == 0:
        break #falta print(lista)

print("Adios")
    

            

        
