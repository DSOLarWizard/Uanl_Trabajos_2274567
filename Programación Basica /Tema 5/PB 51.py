#problema 51

trabajadores = []
asistencia = []

print("Bienvenido al registro de asistencia de mi primera chamba")

print("Para registrar trabajadores elije 1, para ver si asistieron elije 2, para salir elija cuaquier otro numero")

while True:
    x = int(input("Elección:"))

    if x == 1:
        nombre = str(input("Ingrese el nombre del trabajador:"))
        asist = int(input("Si asistio elija 1, si falto elija 0:"))

        trabajadores.append(nombre)
        asistencia.append(asist)
        
    elif x == 2:
        y = str(input("ingrese el nombre del trabajador"))
        z = trabajadores.index(y)

        print(trabajadores[z],"...")
        if asistencia[z] == 1:
            print("Asistio a trabajar")
        elif asistencia[z] == 0:
            print("Falto a la chamba")
        else:
            print("Error de registro")

    else:
        break

print("Adios y te la lavas bb")
