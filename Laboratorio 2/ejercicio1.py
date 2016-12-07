#-*-coding:utf-8 -*-
#Laboratorio 2
#Alejandro Romero Amezcua
#25 de noviembre de 2016
import math
cateto1=float(input("Ingrese el primer cateto: "))
cateto2=float(input("Ingrese el segundo cateto: "))
def obteherh(a,b):
    hipotenusa=float
    hipotenusa=math.sqrt((a*a)+(b*b))
    return hipotenusa
print "La hipotenusa del triangulo con catetos: ",cateto1," y ",cateto2," es: ",obteherh(cateto1,cateto2)
