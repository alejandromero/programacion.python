#-*-coding:utf-8 -*-
#Laboratorio 1
#Alejandro Romero Amezcua
#Ejercicio3
areacirculo=0
volumenesfera=0
pi=3.14159265359
r=int(input("Introdusca el radio del circulo/esfera: "))
def area(a):
    areacirculo=pi*a*a
    return areacirculo
def volumen(a):
    volumenesfera=(4/3)*pi*a*a*a
    return volumenesfera
print "El area del circulo es: ",area(r)
print "El volumen de la esfera es:",volumen(r)