# problema 56

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = max(numeros)

print(numeros)

for i in range(10):
    x += 1
    numeros.append(x)

print(numeros)
