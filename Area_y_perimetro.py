import math

def area_del_rectangulo_y_circulos (a=float, b=float, r=float)->float:
    area_total = ((a*b)+(2*(math.pi*r**2)))
    return area_total

def perimetro_del_rectangulo_y_circulos (a=float, b=float, r=float)->float:
    perimetro_total = ((2*a + 2*b) + (2*(2*math.pi*r)))
    return perimetro_total

if __name__ == "__main__":
    a=float(input("Ingrese la altura del rectangulo: "))
    b=float(input("Ingrese el largo del rectangulo: "))
    r=float(input("Ingrese el radio de los circulos: "))

area = area_del_rectangulo_y_circulos (a,b,r)
print("El area que tiene el rectangulo de altura "+str(a)+" y de base "+str(b)+" junto a dos circulos de radio "+str(r)+" es de "+str(area))

perimetro = perimetro_del_rectangulo_y_circulos(a,b,r)
print("El perimetro que tiene el rectangulo de altura "+str(a)+" y de base "+str(b)+" junto a dos circulos de radio "+str(r)+" es de "+str(perimetro))
