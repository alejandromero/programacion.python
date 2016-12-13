#-*-coding:utf-8 -*-
#Ejercicio 3
#Alejandro Romero Amezcua
#12 de diciembre de 2016
"""Programa que que regresa un nuevo archivo con nombres cocatenados"""

def newfile(cont,nombre):
	newf=open(nombre,"w")
	newf.write(cont[0])

def concatenar(l):
	c=[]
	for j in range(0,len(l)):
		if j==0:
			c.append(l[j])
		else:
			c[0]=c[0]+l[j]
			print
	return c

nombre=raw_input("\n¿Cual sera el nombre del archivo?\n")
nombre=nombre+'.txt'
n=int(raw_input("¿Cuantos nombres de archivos introducira?\n"))
nombres=[]
for i in range(0,n,1):
	print "Ingrese el ",i+1," nombre: "
	nombres.append(raw_input())
contenido=concatenar(nombres)
newfile(contenido,nombre)

raw_input("\nPresione la tecla intro para terminar la ejecucion")