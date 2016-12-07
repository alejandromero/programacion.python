#-*-coding:utf-8 -*-
#Laboratorio 1
#Alejandro Romero Amezcua
#Ejercicio5
segundos=(int(input("Introduzca el numero de segundos totales: ")))
def conversion(a):
	tiempo=[]
	residuo=0
	tiempo.append(a/84600)
	residuo=a%84600
	tiempo.append(residuo/3600)
	residuo=a%3600
	tiempo.append(residuo/60)
	residuo=residuo%60
	tiempo.append(residuo)
	return tiempo
print conversion(segundos)