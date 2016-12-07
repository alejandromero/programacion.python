#Ejercicio 1d
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
import math
t=np.linspace(0,24,100)
y=[]
for i in range(0,len(t)):
	z=math.e**(-.1*t[i])*math.sin(2*t[i]) #Una forma de solucionar el error, otras seria poner np antes del sen
	y.append(z)
plt.figure("Ejercicio 1d")
plt.plot(t,y,linewidth=7,color='k',label='Grafica de h(t)')
plt.legend()
plt.title("e^-2t sen(2t)")
plt.xlabel('t=[0,24]')
plt.ylabel('f(t) evaluada desde t=0 hasta t=24')
plt.grid(True)
plt.show()