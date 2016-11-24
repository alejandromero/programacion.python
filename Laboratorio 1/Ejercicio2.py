#Laboratorio 2
#Alejandro Romero Amezcua
#Ejercicio 2
saldoinicial=float(input("Introducir saldo inicial: "))
anos=int(input("A cuantos tiempo quiere ver el aumento del saldo inicial "))
saldoanos=[]
def interes(a):
    a=(a*.04)+a
    return a
for i in range(0,anos):
    saldoinicial=interes(saldoinicial)
    saldoanos.append(interes(saldoinicial))
print saldoanos
