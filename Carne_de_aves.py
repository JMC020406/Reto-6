def cuantos_kg_de_aves_tenemos (n=int, m=int, k=int)->int:
    total_kg = n*6 + m*7 + k*1
    return total_kg

if __name__ == "__main__":
    n=int(input("Ingrese la cantidad de gallinas que tiene: "))
    m=int(input("Ingrese la cantidad de gallos que tiene: "))
    k=int(input("Ingrese la cantidad de pollitos que tiene: "))

carne_de_aves = cuantos_kg_de_aves_tenemos(n,m,k)
print("Teniendo "+str(n)+" gallinas, "+str(m)+" gallos y "+str(k)+" pollitos, entonces tenemos "+str(carne_de_aves)+" kilogramos de carne")
