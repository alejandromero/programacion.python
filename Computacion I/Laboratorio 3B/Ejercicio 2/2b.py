#-*-coding:utf-8 -*-
#Ejercicio 2b
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
import math
x=np.linspace(0,2,100)
f=x*math.e**(-3*x)
g=(math.e**(-3*x))*(1-3*x)
plt.figure("Ejercicio 1b")
plt.plot(x,f,linewidth=7,color='cyan',label='Grafica de f(x)')
plt.legend()
plt.plot(x,g,linewidth=7,color='b',label='Grafica de g(x)')
plt.legend()
plt.title("Comparacion de f(x) y g(x)")
plt.xlabel('x=[0,2]')
plt.ylabel('f(x) y g(x)')
plt.grid(True)
plt.show()