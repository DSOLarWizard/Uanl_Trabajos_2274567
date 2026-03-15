#problema 64 - funcion EsMultiplo

def EsMultiplo(a,b):
    if b % a == 0:
        return a,"es multiplo de", b
    else:
        return a, "no es multiplo  de", b

print("prueba de multiplos, ingrese el numero que se quiere factorizar y el posible factor")
x = float(input("factorizado:"))
y = float(input("posible factor:"))

print(EsMultiplo(y,x),"por ende, se puede factorizar :D")
