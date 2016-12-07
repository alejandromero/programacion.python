#-*-coding:utf-8 -*-
#Ejercicio 3b
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi
t=(pi*(np.linspace(-360,360,720)))/180
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
plt.figure("Ejercicio 3b")
plt.plot(t,x,linewidth=5,color='grey',label='Grafica de X(t)')
plt.legend()
plt.plot(t,y,linewidth=6,color='k',label='Grafica de Y(t)')
plt.legend()
plt.title("X vs Y")
plt.xlabel('x=[-2pi,2pi]')
plt.ylabel('X(t) y Y(t)')
plt.grid(True)
plt.show()