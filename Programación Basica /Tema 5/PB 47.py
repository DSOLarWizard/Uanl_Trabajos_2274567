#problema 47

Cardex = {}
clifs = []
materia = "1"

print("hoy es día de hacer la boleta de calificaciones")

while materia != "0":
    print("ingrese una materia o '0' para terminar de añadir datos")
    materia = input("materia:")
    if materia != "0":
        print("ingrese calificaciones a promediar o un numero negativo para terminar")
    while True and materia != "0":
        calif = int(input("calificación:"))
        if calif >= 0:
            clifs.append(calif)
        if calif < 0:
            promedio = sum(clifs)/len(clifs)
            break
    if materia !="0":
        Cardex[materia] = promedio
print("su boleta de calificaciónes sería la siguiente",Cardex)
        
        
        
