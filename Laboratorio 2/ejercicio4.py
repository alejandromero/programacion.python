#Laboratorio 2
#Alejandro Romero Amezcua
#25 de noviembre de 2016
import math
lados=int(input("Numero de lados: "))
longitud=float(input("Cual sera la longitud de los lados: "))
incrementoangulo=0
x=[]
y=[]
def llenar(a,x,y): #Llenar los arrays con el numero de coordenadas que se ocupan
  for i in range(0,a):
    x.append(0)
    y.append(0)
  return x,y
llenar(lados,x,y)
def iangulo(a): #Calcular los angulos internos entre cada arista
  global incrementoangulo
  incrementoangulo=((2*math.pi)/a)
iangulo(lados)
def imprimirc(x,y): #Imprimir los arrays que contienen las coordendas 
  for i in range(0,len(x)):
    print "Verice ",i+1,": ",x[i],",",y[i]
def coordenadas(a,l,b,x,y): #Calcular las coordenadas de cada punto
  lx=0
  ly=0
  ta=0
  for i in range(0,a):
    lx=l*math.cos(ta) 
    if lx<.0000000009 and lx>-.0000000009: #Arreglar falta de decimales
      lx=0.0
    #print "x: ",lx #ver valor de lado x
    ly=l*math.sin(ta)
    if ly<.0000000009 and ly>-.0000000009:
      ly=0.0
    #print "y: ",ly #ver valor de lado y
    ta=ta+b
    if i==0:
      x[i]=lx
      y[i]=ly
    elif i==a-1: #Arreglar problema de exponentes negativos
      x[i]=0
      y[i]=0
    else:
      x[i]=lx+x[i-1]
      y[i]=ly+y[i-1]
  imprimirc(x,y)
coordenadas(lados,longitud,incrementoangulo,x,y)
