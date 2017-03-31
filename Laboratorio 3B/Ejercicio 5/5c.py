#-*-coding:utf-8 -*-
#Ejercicio 5c
#Alejandro Romero Amezcua
#02 de diciembre de  2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt
a=((np.linspace(0,360))*pi)/180
r=2-2*np.sin(a)+np.sin(a)*((np.sqrt(np.absolute(np.cos(a))))/(np.sin(a))+1.4)
x=r*np.cos(a)
y=r*np.sin(a)
plt.figure('Ejercicio 5c')
plt.plot(a,x,color='brown',label='Grafica se X')
plt.legend()
plt.plot(a,y,color='violet',label='Grafica de Y')
plt.legend()
plt.fill_between(a,x,y,color='red')
plt.title('X vs Y')
plt.xlabel('x=[0,2pi]')
plt.ylabel('y dado por X y Y')
#plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
