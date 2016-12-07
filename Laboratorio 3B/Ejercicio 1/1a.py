#-*-coding:utf-8 -*-
#Ejercicio 1a
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-6,2,100)
y=5-(x*4)-(x*x)
plt.figure("Ejercicio 1a")
plt.plot(x,y,linewidth=5,color='r',label='Grafica de f(x)')
plt.legend()
plt.title("f(x)=5-4x-x^2")
plt.xlabel('x=[-6,2]')
plt.ylabel('Resultados de f(x)')
plt.grid(True)
plt.show()