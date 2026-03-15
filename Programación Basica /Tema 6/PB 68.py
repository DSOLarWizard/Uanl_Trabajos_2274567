#problema 68 - programa que identifica si un numero es primo

def esprimo(x):
    fact = 2
    if x > 3:
        while True:
            if x % fact == 0:
                final = "NOOOOOO ES PRIMO"
                break
            if fact < x:
                fact += 1
            if fact >= x:
                final = "ES PRIMO"
                break
    elif x == 1:
        final = "el uno no cuenta"
    else:
        final = "Es primo"
    return final
        

print("maquina de primos, es su numero primo? averiguemoslo, para salir elija 0")
test = 1
while True:
    test = int(input("numero a pruebaa\n:"))
    if test == 0:
        break
    else:
        print(esprimo(test))

print("bueno bye")
    
