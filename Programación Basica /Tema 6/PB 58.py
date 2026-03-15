#58 - crear una función para llenar una lista de numeros

def llenador_de_listas(lista,relleno):
    lista.append(relleno)

lista1 = []
while True:
    relleno = int(input("ingrese numeros a la lista,para finalizar elija 0 \n:"))
    if relleno == 0:
        break
    else:
        llenador_de_listas(lista1,relleno)

print(lista1)

