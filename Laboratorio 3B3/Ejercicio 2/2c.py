#Ejercicio 2c
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi
x=(pi*(np.linspace(0,720,720)))/180
f=(np.sin(3*x))*(np.cos(2*x))
g=.5*np.cos(x)+(5/2)*np.cos(5*x)
plt.figure("Ejercicio 1c")
plt.plot(x,f,linewidth=5,color='cyan',label='Grafica de f(t)')
plt.legend()
plt.plot(x,g,linewidth=6,color='g',label='Grafica de g(t)')
plt.legend()
plt.title("Comparacion de f(t) y g(t)")
plt.xlabel('x=[0,4pi]')
plt.ylabel('f(t) y g(t)')
plt.grid(True)
plt.show()