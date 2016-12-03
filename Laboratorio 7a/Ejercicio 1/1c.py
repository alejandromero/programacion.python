#Ejercicio 1c
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
import math
t=np.linspace(-1,5,100)
y=t*math.e**(-2*t)
plt.figure("Ejercicio 1c")
plt.plot(t,y,linewidth=5,color='b',label='Grafica de f(t)')
plt.legend()
plt.title("f(t)=te^-2t")
plt.xlabel('t=[-1,5]')
plt.ylabel('f(t) evaluada desde t=-1 hasta t=5')
plt.grid(True)
plt.show()