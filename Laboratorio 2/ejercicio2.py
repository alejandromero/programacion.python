#Laboratorio 2
#Alejandro Romero Amezcua
#25 de noviembre de 2016
distancia=float(input("Ingrese la distancia que recorrio(Km): "))
def conversion(a):
    a=(a*1000)/250
    return a
def pagar(a):
    banderazo=8.74
    total=banderazo+(conversion(a)*1.84)
    print total
pagar(distancia)
