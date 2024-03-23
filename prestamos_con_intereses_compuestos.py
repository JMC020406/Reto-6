def prestamos_con_intereses_compuestos (c=int, i=int, n=int)->int:
    platitaaa = c*(1+i/100)**n
    return platitaaa

if __name__ == "__main__":
    c=int(input("Cuanta plata tiene en su prestamo?: "))
    i=int(input("Cual es el interes el cual afecta ese prestamo (poner el valor de arriba de la fraccion del %)?: "))
    n=int(input("Cuantos meses van a transcurrir?: "))

platitaaa_final = prestamos_con_intereses_compuestos(c,i,n)
print("Tu prestamo de "+str(c)+" en "+str(n)+" meses por su interes del "+str(i)+"% va a tener un valor de "+str(platitaaa_final))
