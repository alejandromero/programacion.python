#Ejercicio 7
#Alejandro Romero Amezcua
#02 de diciembre de 2016
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt
a=((np.linspace(0,720,2000,.04))*pi)/180
r=105+100*(np.sin(4.5*a))
on=a-((np.cos(10*a))/10)
x=320+(r*np.cos(on))
y=-240-(r*np.sin(on))
#plt.axis('equal')
plt.axis('off')
plt.plot(a,x,color='red',label='Grafica se X')
plt.legend()
plt.plot(a,y,color='brown',label='Grafica de Y')
plt.legend()
plt.title('X vs Y')
plt.xlabel('x=[0,4pi]')
plt.ylabel('y dado por X y Y')
plt.grid(True)
plt.show()