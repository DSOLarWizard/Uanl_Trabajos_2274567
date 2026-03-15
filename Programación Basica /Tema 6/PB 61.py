#problema 61 - función que calcule el perimetro de un triangulo

def perimetro_rect(b,h):
    p = 2*b +2*h
    return p


print("Calculadora geometrica del perimetro de un rectangulo a sus ordenes, ingrese los valores de base y altura")
while True:
    B = float(input("Base ="))
    H = float(input("Altura ="))
    print("el perimetro de su cuadrilatero es igual a",perimetro_rect(B,H))
    det = int(input("para finalizar elija 0, para calcular mas perimetros elija cualquier otro numero"))
    if det ==  0:
        break
print("C ya later")
    
    
