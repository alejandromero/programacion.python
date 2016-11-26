#Laboratorio 2
#Alejandro Romero Amezcua
#25 de noviembre de 2016

import matplotlib.pyplot as plt
import numpy as np
import math

print "\n"

longitudlado=float(input("Cual sera la longitud de los lados del triangulo: "))
vertice1=[]
vertice2=[]
vertice3=[]
p0=[]
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
	triangulo=plt.Polygon(vertices,fill=None)
	plt.gca().add_patch(triangulo)
	plt.axis('scaled')
	#plt.show()
def contienep(p,f): #Verifica que el punto este dentro del triangulo
	f.contains_point(p)
def p0r(p,x,y,z,f): #Elige un punto al azar
	i=0
	while i<=2:
		if i==0:
			p.append(np.random.uniform(x[i],y[i]))
		else:
			p.append(np.random.uniform(x[i],z[i]))
			if contienep(p,f)==True:
				pass
			else:
				i=0
		i=i+1
	return p
construirt(longitudlado,vertice1,vertice2,vertice3)
p0r(p0,vertice1,vertice2,vertice3,triangulo)
print p0