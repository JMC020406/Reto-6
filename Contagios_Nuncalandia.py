def contagios_en_nuncalandia (d=int, c=int)->int:
    enfermos= c*2**d
    return enfermos

if __name__ == "__main__":
    c=int(input("Numero de contagiados por covid-19 hasta el momento: "))
    d=int(input("Numero de dias para calcular: "))

enfermos_totales = contagios_en_nuncalandia (d,c)
print("Todo empezo con solo "+str(c)+" habitantes contagiados de covid-19 en Nuncalandia,pero todo eso cambiara, ya que se tiene esperado que para el dia "+str(d)+" aquella cifra aumente hasta "+str(enfermos_totales)+" enfermos totales")
