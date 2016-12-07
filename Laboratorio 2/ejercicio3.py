#-*-coding:utf-8 -*-
#Laboratorio 2
#Alejandro Romero Amezcua
#25 de noviembre de 2016

import matplotlib.pyplot as plt
import numpy as np
import math

print "\n"

longitudlado=float(input("Cual sera la longitud de los lados del triangulo: "))
repeticiones=int(input("Cuantas veces se repetira el proceso: "))
vertice1=[]
vertice2=[]
vertice3=[]
p0=[0,0]
p1=[]
totalpuntosx=[]
totalpuntosy=[]
def verticesc23(a,x,y,z): #Obtiene los vertices faltantes del triangulo
	vertice1.append(input("Cual sera la coordenada x para el vertice inicial: "))
	vertice1.append(input("Cual sera la coordenada y para el vertice inicial: "))
	for i in range(0,len(x)):
		if i==0:
			y.append((a*math.cos((0*math.pi)/180))+x[i])
			z.append((a*math.cos((120*math.pi)/180))+y[i])
		else:
			y.append((a*math.sin((0*math.pi)/180))+x[i])
			z.append(a*math.sin((120*math.pi)/180)+y[i])
	return x,y,z

def construirt(a,x,y,z): #Construye el triangulo con los vertices dados
	global triangulo
	verticesc23(a,x,y,z)
	vertices=[vertice1,vertice2,vertice3]
	plt.figure('Juego del caos')
	triangulo=plt.Polygon(vertices,fill=None)
	
def p0r(p,x,y,z): #Elige un punto al azar
	p[0]=(np.random.uniform(x[0],y[0]))
	p[1]=(np.random.uniform(x[1],z[1]))
	return p

def contienep(p,f): #Verifica que el punto este dentro del triangulo
		if f.contains_point(p)==True:
			return 1
		else:
			return 0

construirt(longitudlado,vertice1,vertice2,vertice3)

def azarv(x,y,z): #Seleccionar vertice al azar
	vertices=[x,y,z]
	verticeazar=vertices[np.random.randint(0,3)]
	return verticeazar
def puntom(p,v,p1,tpx,tpy):
	p1=[]
	for i in range(0,len(v)):
		if i==0:
			p1.append((p[i]+v[i])/2)
		else:
			p1.append((p[i]+v[i])/2)
	p[0]=p1[0]
	p[1]=p1[1]
	tpx.append(p1[0])
	tpy.append(p1[1])
	return p
	return p1
	return tp
	
def imprimir(t,tpx,tpy): #Imprime el triangulo y los puntos en la pantalla
	plt.figure('Juego del caos')
	plt.gca().add_patch(t)
	plt.scatter(tpx,tpy)
	plt.axis('scaled')
	plt.show()

j=0
while j==0: #Asegurar que p0(inicial) este dentro del triangulo
	p0r(p0,vertice1,vertice2,vertice3)
	if contienep(p0,triangulo)==1:
		j=1
	else:
		pass

for i in range(0,repeticiones):
	puntom(p0,azarv(vertice1,vertice2,vertice3),p1,totalpuntosx,totalpuntosy)
#print "\n",totalpuntosx,"\n",totalpuntosy	
imprimir(triangulo,totalpuntosx,totalpuntosy)
