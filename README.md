# Reto-6
## Funciones 1
Para este punto de las clases de programación ya nos exigieron ser más ordenados de lo que eramos antes con todo el desparrame de codigo que tenian nuestros programas. Ahora ya nos han explicado lo básico para crear una función, llamarla y aplicarle valores. 
En este reto se hacen un total de 7 programas con multiples funciones dentro de ellos y varios pasos extra como consultar que es *pip* y hacer un listado de modulos populares en este.

### Punto 1 / El volumen y el área superficial de una esfera y un cono
```py
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
```
Para este primer punto se exigieron un total de 3 cosas: Primero se exigio el poder hacer una función matemática en la cual se pudiera calcular el volumen de una esfera más un cono, y otra función que usara los mismo datos pero para calcular el area suferficial de las figuras. Una vez ya encontradas esas dos funciones que nos ayudan a calcular el volumen y el area superficial habia que definirlas a modo de funcion en python. Por ultimo, si uno sigue este paso a paso se dara cuenta que le falta el dato π (pi) en sus funciones, haciendo que uno tenga la necesidad de importar su valor desde la librería de *math*. Entonces una vez importada la librería uno debe escribir *math.pi* para que python interprete a nuestro querido π.

### Punto 2 / El área y perimetro de un rectángulo y dos círculos
```py
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
```
Este punto es muy similar al previo así que no hay mucho que explicar, lo único que cambia es que se resta una dimensión en los objetos. Toca nuevamente sacar una función que nos ayude a calcular el área de un rectángulo y dos círculos, y otra la cual sea para el perímetro. Luego definirlas corectamente en python. Por último importar nuevamente a nuestro querido π.

### Punto 3 / ¿Cuántos Kg de carne de ave tenemos?
```py
def cuantos_kg_de_aves_tenemos (n=int, m=int, k=int)->int:
    total_kg = n*6 + m*7 + k*1
    return total_kg

if __name__ == "__main__":
    n=int(input("Ingrese la cantidad de gallinas que tiene: "))
    m=int(input("Ingrese la cantidad de gallos que tiene: "))
    k=int(input("Ingrese la cantidad de pollitos que tiene: "))

carne_de_aves = cuantos_kg_de_aves_tenemos(n,m,k)
print("Teniendo "+str(n)+" gallinas, "+str(m)+" gallos y "+str(k)+" pollitos, entonces tenemos "+str(carne_de_aves)+" kilogramos de carne")
```
Este punto lo único que nos exigía era crear correctamente la función la cual calcula cuanta carne se tiene si cada gallina pesa 6Kg, cada gallo 7Kg y cada pollito 1Kg. Que no le ví la necesidad de involucrar a los pollitos, eso no esta cool >:(.

### Punto 4 / Cuentas del supermercado
```py
def cuentas_del_mercado (p=int, m=int, h=int, b=int)->int:
    cuentas= b-(p*300+m*3300+h*350)
    return cuentas

if __name__ == "__main__":
    p=int(input("Cuantos panes vas a comprar?: "))
    m=int(input("Cuantas bolsas de leche vas a comprar?: "))
    h=int(input("Cuantos huevos vas a comprar?: "))
    b=int(input("Cuanta plata te dio tu mama?: "))

recibo = cuentas_del_mercado (p, m, h, b)

if recibo>0:
    print("vaya te sobraron "+str(recibo)+" pesos , tal vez puedas comprarte algo con eso")
elif recibo<0:
    print("Diablos, quedamos debiendo "+str(-1*recibo)+" pesos, habra que ir a pedirle mas dinero a mama")
else:
    print("Que maravilla! Las cuentas fueron exactas. Mama se pondra feliz al saber que te sobraron "+str(recibo)+" pesos")
```
El típico problema matemático de si tienes tanto dinero ¿cuantas cosas x puedes comprar? Aun así, es entretenido de hacer estos programas y luego a la hora de probrarlos darse cuenta de que si le estan funcionando a uno. Es sencillamente maravilloso!

Y el paso a paso para hacer es codigo es: Definir el función, definir variables, llamar función y escribir resultado; y que no falte el contexto de los datos en esos resultados.

### Punto 5 / Prestamos con Intereses compuestos
```py
def prestamos_con_intereses_compuestos (c=int, i=int, n=int)->int:
    platitaaa = c*(1+i/100)**n
    return platitaaa

if __name__ == "__main__":
    c=int(input("Cuanta plata tiene en su prestamo?: "))
    i=int(input("Cual es el interes el cual afecta ese prestamo (poner el valor de arriba de la fraccion del %)?: "))
    n=int(input("Cuantos meses van a transcurrir?: "))

platitaaa_final = prestamos_con_intereses_compuestos(c,i,n)
print("Tu prestamo de "+str(c)+" en "+str(n)+" meses por su interes del "+str(i)+"% va a tener un valor de "+str(platitaaa_final))
```
Como siempre: Definir función, definir variables, llamar función y escribir resultados de una menra creativa y llena de sazón 🧑‍🍳

### Punto 6 / Contagios en Nuncalandia
```py
def contagios_en_nuncalandia (d=int, c=int)->int:
    enfermos= c*2**d
    return enfermos

if __name__ == "__main__":
    c=int(input("Numero de contagiados por covid-19 hasta el momento: "))
    d=int(input("Numero de dias para calcular: "))

enfermos_totales = contagios_en_nuncalandia (d,c)
print("Todo empezo con solo "+str(c)+" habitantes contagiados de covid-19 en Nuncalandia,pero todo eso cambiara, ya que se tiene esperado que para el dia "+str(d)+" aquella cifra aumente hasta "+str(enfermos_totales)+" enfermos totales")
```
En este programa le puse harto sazón a los resultados, pero bueno. En este caso la población de va contagiando el doble cada día que transcurre, de una manera *exponencial*, lo cual nos dice ya todo para hacer la función, que es, tomar los contagiados por covid-19 desde un inicio y cada dia que transcurre multiplicarlo por 2.
Luego para continuar con el código hay que deinir variables y etc, etc. 

### Punto 7 / Operar y Ordenar 5 números cualquiera (*sufrimiento interno*) 
