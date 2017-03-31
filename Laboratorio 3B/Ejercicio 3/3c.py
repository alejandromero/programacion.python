#-*-coding:utf-8 -*-
#Ejercicio 3c
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi
t=(pi*(np.linspace(0,360,360)))/180
x=np.sin(3*t)
y=np.cos(4*t)
plt.figure("Ejercicio 3c")
plt.plot(t,x,linewidth=5,color='orange',label='Grafica de X(t)')
plt.legend()
plt.plot(t,y,linewidth=7.2,color='yellow',label='Grafica de Y(t)')
plt.legend()
plt.title("X vs Y")
plt.xlabel('x=[0,2pi]')
plt.ylabel('X(t) y Y(t)')
plt.grid(True)
plt.show()