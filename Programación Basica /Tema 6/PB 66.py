#problema 66 - filtro de reprobados

def filtro(dicc):
    fail = []
    for x in dicc:
        if dicc[x] < 70.0:
            fail.append(x)
    return fail
calif = dict()
calif1 = {"pepito": 70.0, "juanito" : 30.0, "Monchito" : 67.0, "josefina": 90.0, "la popis": 3.0}

print("para una prueba rapida elija 1, para una personalizada elija cualquier otro numero")
path = int(input(":"))
if path == 1:
    print("de los alumnos",calif1,"reprobaron",filtro(calif1))
else:
    print("ingrese pares de nombre y calificaación o ingrese -1 en cualquiera de las 2 para finalizar")
    while True:
        alum = str(input("nombre:"))
        grade = float(input("calificación:"))
        if alum != "-1" and grade != -1.0:
            calif[alum] = grade
        else:
            break
    print("han reprobado",filtro(calif))
print("fin de la wea esta")
