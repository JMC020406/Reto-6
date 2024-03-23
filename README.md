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
Este punto del reto contiene internamente unas 7 funciones a definir, lo cual me traen malos recuerdos del Taller 1 que hicimos en grupos. Sin embargo este caso es más fácil ya que aquí no estamos limitados a solo usar condicionales para solucionar este problema, así que adelante.
```py
# Funciones

def promedio_5 (a=float,b=float,c=float,d=float,e=float)->float:
    calculo_promedio= ((a+b+c+d+e)/5)
    return calculo_promedio

def mediana_5(a=float,b=float,c=float,d=float,e=float)->float:
    numeros_ordenados=sorted(lista_numeros)
    n=len(numeros_ordenados)
    calculo_mediana = n//2
    return numeros_ordenados[calculo_mediana]

def promedio_multiplicativo_5(a=float,b=float,c=float,d=float,e=float)->float:
    calculo_promedio_multiplicativo=((a*b*c*d*e)**(1/5))
    return calculo_promedio_multiplicativo

def ordenados_ascendente_5 (a=float,b=float,c=float,d=float,e=float)->float:
    ascendente=sorted(lista_numeros)
    return ascendente

def ordenados_descendente_5 (a=float,b=float,c=float,d=float,e=float)->float:
    descendente=sorted(lista_numeros, reverse=True)
    return descendente

def elevado_mayor_al_menor_5(a=float,b=float,c=float,d=float,e=float)->float:
    mayor_elevado_al_menor= max(lista_numeros)**min(lista_numeros)
    return mayor_elevado_al_menor

def menor_elevado_3_5 (a=float,b=float,c=float,d=float,e=float)->float:
    menor_elevado_3= min(lista_numeros)**3
    return menor_elevado_3

if __name__ == "__main__":

#Definicion de variables

    a=float(input("Ingrese el primer numero: "))
    b=float(input("Ingrese el segundo numero: "))
    c=float(input("Ingrese el tercer numero: "))
    d=float(input("Ingrese el cuarto numero: "))
    e=float(input("Ingrese el quinto numero: "))

lista_numeros = (a,b,c,d,e)

# Llamado de las funciones y resultados

promedio = promedio_5(a,b,c,d,e)
print("El valor del promedio es "+str(promedio))

mediana = mediana_5(a,b,c,d,e)
print("La mediana es "+str(mediana))

promedio_multiplicativo = promedio_multiplicativo_5(a,b,c,d,e)
print("El valor del promedio multiplicativo es "+str(promedio_multiplicativo))

ordenados_ascendente = ordenados_ascendente_5(a,b,c,d,e)
print("Ordenados de manera ascendente: "+str(ordenados_ascendente))

ordenados_descendente = ordenados_descendente_5(a,b,c,d,e)
print("Ordenados de manera descendente: "+str(ordenados_descendente))

mayor_elevado_al_menor = elevado_mayor_al_menor_5(a,b,c,d,e)
print("La potencia del numero mayor elevado al menor es "+str(mayor_elevado_al_menor)) 

menor_elevado_al_cubo = menor_elevado_3_5(a,b,c,d,e)
print("El numero menor elevado al cubo es: "+str(menor_elevado_al_cubo))
```
Entonces para este punto habia, como ya dije, que definir 7 funciones en total: El promedio, La mediana, El promedio multiplicativo, Ordenar de manera ascendente y descendente, Elevar el numero mayor al menor y elevar numero menor al cubo.

Para lograrlo use medios matematicos (para "el promedio", "promedio multiplicativo", "mayor elevado al menor" y "menor al cubo"), tuve que definir la lista de los numero seleccionados para poder luego organizarlos con la funcion *sorted* y poder sacarle la mediana con la funcion *len()* (fueron usados para "la mediana, "ordenar de manera ascendente" y "ordenar de manera descendente") ,y use las palabras reservadas *max* / *min* para determinar el numero mayor / menor de la lista (para "el numero mayor elevado al menor" y "numero menor al cubo")

### Punto 8 / Crear un archivo independiente de las funciones del punto 7 e importarlas
En los archivos de este repositorio se encontrara el archivo *inportar.py* que son las funciones del ejercicio 7 para importar.

### Punto 9 / ¿Qué es *pip* en python?
*pip* en python es el sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Esos paquetes de software son los modulos y librerias las cuales se pueden importar a nuestros archivos gracias a que estan subidos en un nube. Entonces, *pip* da cierta ventaja a la hora de instalar o actualizar paquetes, además de la gestión entre ellos.

Para cada uno de las cosas antes mencionadas que nos permite *pip* hay que ingresar cierto codigo al programa de python, lo cual incluye: Instalación de prgramas, actualización de programas, eleminar paquetes y consultar paquetes instalados.

    1)Instalar un paquete: pip install nombre_del_paquete
    
    2)Actualizar un paquete: pip install –upgrade nombre_del_paquete
    
    3)Desinstalar un paquete: pip uninstall nombre_del_paquete
    
    4)Listar paquetes instalados: pip list

Por esta accesibilidad que le da a los programadores a otros paquetes que les pueden ser necesarios es que se considera que *pip* es algo indispensable para los trabajos y trabajadores de programación que se hacen en python.

Información sacada de: https://abcxperts.com/que-es-pip/ 

### Punto 10 / ¿Cuáles son los paquetes más famosos de *pip*?
Como ya mencione previamente, para instalar un paquete *pip* lo que hay que hacer es escribir en el código de python *pip install "nombre_del_paquete"*. En "nombre_del_paquete" es donde va, claramente, el nombre de la librería o módulo que queremos incluir en nuestro programa. Los más descargados, es decir, también los más utiles son los siguientes:

    1)Pandas                (Manejo de datos)
    2)Numpy                 (Operar matrices)
    3)Plotly                (Imagen y clic)
    4)Scikit-learn          (Machine Learning en tu mano)
    5)Category-encoders     (Mejora del Dato)
    6)Imbalance Learning    (Emparejar los datos)
    7)LightGBM / XGBoost    (Árboles con potencia)
    8)Keras / Tensorflow    (Deep Learning en pocas líneas)
    9)Shap                  (Intepretación de modelos)
    10)AzureML-sdk          (Implementación ML en la Nube)
    
Y como se puede leer cada una tiene una función especifica, así que lo más recomendado sería tener un buen listado de paquetes de *pip* para que tu trabajos se faliciten.

Fuente: https://verneacademy.com/blog/articulos-ia/10-librerias-python-data-science-machine-learning/
