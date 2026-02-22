#problema 46

numeros = []
cuadrados = []
y = 0

while y < 10:
    entrada = float(input("ingrese un numero para la lista de que elevar a la 2da potencia:"))
    numeros.append(entrada)
    y += 1

for x in numeros: #"x" y "entrada" son lo mismo
    num_elevados = x**2 
    cuadrados.append(num_elevados)

print("el cuadrado de los numeros",numeros,"sería",cuadrados)

#que aprendimos el dia de hoy?:

#1. las listas se llenan usando un ciclo, una variable y lista.append(variable)

#2. la funcion for puede leer X como cada objeto de una lista y de este modo hacer operaciones con ellos ( y meterlos a otra lista siasi se desea)
