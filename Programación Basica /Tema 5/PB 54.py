#problema 54

ahorradores = ["Hermenegildo","Gertrudiz","Encarnación"]
ahorros = [200789.0,572.0,2780000.0]

for x in ahorradores:
    y =  ahorradores.index(x)

    if ahorros[y] < 1000:
        print(ahorradores[y],", no tendrás para tu futuro")
    elif ahorros[y] > 1000000:
        print(ahorradores[y],",ya merito te retiras")
    else:
        print(ahorradores[y],",plata neutra, ni fu ni fa")
    

