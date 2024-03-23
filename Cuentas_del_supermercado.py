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

