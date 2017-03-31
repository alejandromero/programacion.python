#-*-coding:utf-8 -*-
#Ejercicio 6
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt
a=((np.linspace(0,360,1000,.015))*pi)/180
r=-250*(np.sin(5*a))*(np.cos(4*a))
on=a+np.sin(r/100)
x=320+(r*np.cos(on))
y=-240-(r*np.sin(on))
plt.figure('Ejercicio 6')
plt.plot(a,x,color='red',label='Grafica se X')
plt.legend()
plt.plot(a,y,color='brown',label='Grafica de Y')
plt.legend()
plt.axis('off')
#plt.axis('equal')
plt.title('X vs Y')
plt.xlabel('x=[0,2pi]')
plt.ylabel('y dado por X y Y')
plt.grid(True)
plt.show()