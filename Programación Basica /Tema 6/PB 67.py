#67676767676767676767676767
#ordena creciente y decreciente
#elimmina por indice
#elimina por  dato
#calula promedio, max y min

def ordenUp(lista):
    n = len(lista)
    for i in range(n):
        cambio = False
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                cambio = True
        if not cambio:
            break
    return lista

def ordenDown(lista):
    n = len(lista)
    for i in range(n):
        cambio = False
        for j in range(0,n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                cambio = True
        if not cambio:
            break
    return lista

def eliminaPos(x,lista):
    if x < len(lista):
        del lista[x-1]
    return lista

def eliminaDato(y,lista):
    return[i for i in lista if i != y]

def datos(lista):
    lista1 = ordenUp(lista)
    p = sum(lista)/len(lista)
    maxi = lista[len(lista1)-1]
    mini = lista1[0]
    return p, maxi, mini

print("Bienvenido al asistente de listas numericas, primero pibe, haga su lista y eija 0.69 para completar la lista")
lis =[]
while True:
    num = float(input("añadir:"))
    if num != 0.69:
        lis.append(num)
    else:
        break

print("su lista es",lis)
print("para ordenar de mayor a menor elija 1, para hacer lo opuesto elija 2, para eliminar por posición elija 3, para eliminar por termino, elija 4, para mostrar el promedio, el maximo y el minimo elija 5, para terminar elija cualquier otro numero")

des = 1

while des == 1 or des == 2 or des == 3 or des == 4 or des == 5:
    des = int(input("protocolo:"))

    if des == 1:
        lis = ordenUp(lis)
        print(lis)

    elif des == 2:
        lis = ordenDown(lis)
        print(lis)

    elif des == 3:
        dty = int(input("posición del elemento a eliminar:"))
        lis = eliminaPos(dty,lis)
        print(lis)
        
    elif des == 4:
        target = float(input("elemento a eliminar:"))
        lis = eliminaDato(target,lis)
        print(lis)
    

    elif des == 5:
        print("el promedio, maximo y minimo de la lista son:",datos(lis))
    else:
        break
print("la lista final fue",lis,"\n Que tenga buen día")

    
