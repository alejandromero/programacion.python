#-*-coding:utf-8 -*-
#Laboratorio 2
#Alejandro Romero Amezcua
#29 de noviembre de 20126

import math

lat1=float(input("Ingrese la primera latitud: "))
lon1=float(input("Ingrese la primera longitud: "))
lat2=float(input("Ingrese la segunda latitud: "))
lon2=float(input("Ingrese la segunda longitud: "))

def gar(x1,y1,x2,y2):
	x1=(x1*math.pi)/180
	y1=(y1*math.pi)/180
	x2=(x2*math.pi)/180
	y2=(y2*math.pi)/180
        return x1,y1,x2,y2
    
def dis(x1,y1,x2,y2):
    d=6371.01*math.acos((math.sin(gar(x1,y1,x2,y2)[0]))*(math.sin(gar(x1,y1,x2,y2)[2]))+((math.cos(gar(x1,y1,x2,y2)[0]))*(math.cos(gar(x1,y1,x2,y2)[2]))*(math.cos((gar(x1,y1,x2,y2)[1])-(gar(x1,y1,x2,y2)[3])))))
    return d

print "La distancia entre los puntos ingresados es: ", dis(lat1,lon1,lat2,lon2)," kilometros"