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