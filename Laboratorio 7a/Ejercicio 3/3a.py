#Ejercicio 3a
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi
t=(pi*(np.linspace(0,360,360)))/180
x=(np.cos(t))**3
y=(np.sin(t))**3
plt.figure("Ejercicio 3a")
plt.plot(t,x,linewidth=5,color='pink',label='Grafica de X(t)')
plt.legend()
plt.plot(t,y,linewidth=6,color='red',label='Grafica de Y(t)')
plt.legend()
plt.title("X vs Y")
plt.xlabel('x=[0,2pi]')
plt.ylabel('X(t) y Y(t)')
plt.grid(True)
plt.show()