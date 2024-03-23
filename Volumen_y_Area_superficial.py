import math

def volumen_de_la_esfera_y_cono (r1=float , r2=float , h =float)->float:
    volumen_total = (((3/4)*math.pi*r1**3)+((h/3)*math.pi*r2**2))
    return volumen_total

def area_superficial_de_la_esfera_y_cono (r1=float , r2=float , h=float)->float:
    area_superficial = ((4*math.pi*r1**2)+(((math.pi)*r2*(r2**2+h**2))+(math.pi*r2**2)))
    return area_superficial

if __name__ == "__main__":
    r1=float(input("Ingrese el radio de la esfera: "))
    r2=float(input("Ingrese el radio del cono: "))
    h=float(input("Ingrese la altura del cono: "))

volumen = volumen_de_la_esfera_y_cono (r1, r2 , h)
print("El volumen que tienen la esfera de radio "+str(r1)+" y el cono de radio "+str(r2)+" con altura de "+str(h)+" es de "+str(volumen))

area_superficial = area_superficial_de_la_esfera_y_cono (r1, r2, h)
print("El area superficial que tienen la esfera de radio "+str(r1)+" y el cono de radio "+str(r2)+" con altura de "+str(h)+" es de "+str(area_superficial))
