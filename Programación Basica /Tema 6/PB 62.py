#problema 62 - funcion que reciva calificaciones y regrese el promedio junto a un mensaje reprobatorio

def situacion(a,b,c):
    p = (a+b+c)/3.0
    if p < 70:
        print("te vas a extra, porque tu promedio fue:")
        return p
    else:
        print("felicidades mi estimado sesudo, has logrado un promedio de")
        return p

print("hora de ver como te fueen el periodo escolar, ingresa tus calificaciones")
c1 = float(input("calificación 1\n:"))
c2 = float(input("calificación 2\n:"))
c3 = float(input("calificación 3\n:"))

print(situacion(c1,c2,c3))
