#-*-coding:utf-8 -*-
#Laboratorio 1
#Alejandro Romero Amezcua
#Ejercicio4
segundostotales=0
dias=(int(input("Cuantos dias duro el viaje: ")))
horas=(int(input("Cuanta horas duro el viaje: ")))
minutos=(int(input("Cuantos minutos duroel viaje: ")))
segundos=(int(input("Cuantos segundos duro el viaje: ")))
def convertird(a):
	return a*24*60*60
def convertirh(a):
	return a*60*60
def convertirm(a):
	return a*60
segundostotales=segundostotales+segundos+convertird(dias)+convertirh(horas)+convertirm(minutos)
print segundostotales