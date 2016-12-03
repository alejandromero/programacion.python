import numpy as np
import matplotlib.pyplot as plt

caracontorno=plt.Circle((6,6),6,facecolor='w',linewidth=10)

orejad=plt.Circle((10.5,10.5),3,facecolor='w',linewidth=8)
orejad2=plt.Circle((10.5,10.5),2,facecolor='w',linewidth=8)

orejai=plt.Circle((1.5,10.5),3,facecolor='w',linewidth=8)
orejai2=plt.Circle((1.5,10.5),2,facecolor='w',linewidth=8)

ojod=plt.Circle((9,6.8),3,facecolor='w',linewidth=10)
irisd=plt.plot((9,9),(9.2,4.4),linewidth=35,color='k')

ojoi=plt.Circle((3,6.8),3,facecolor='w',linewidth=10)
irisd=plt.plot((3,3),(9.2,4.4),linewidth=35,color='k')

boca=plt.plot((.5,11.4),(3.7,3.7),linewidth=9,color='k')

diente=plt.plot((1.34,2.68),(2.2,3.7),linewidth=7,color='k')

vertices1=[[2.68,3.7],[3.77,.7],[4.86,3.7]]
diente1=plt.Polygon(vertices1,facecolor='w',linewidth=7)
vertices2=[[4.86,3.7],[5.95,.17],[7.04,3.7]]
diente2=plt.Polygon(vertices2,facecolor='w',linewidth=7)
vertices3=[[7.04,3.7],[8.13,.7],[9.22,3.7]]
diente3=plt.Polygon(vertices3,facecolor='w',linewidth=7)

diente4=plt.plot((9.22,10.7),(3.7,2.2),linewidth=7,color='k')

plt.gca().add_patch(orejad)
plt.gca().add_patch(orejad2)
plt.gca().add_patch(orejai)
plt.gca().add_patch(orejai2)

plt.gca().add_patch(caracontorno)

plt.gca().add_patch(ojod)
plt.gca().add_patch(ojoi)

plt.gca().add_patch(diente1)
plt.gca().add_patch(diente2)
plt.gca().add_patch(diente3)

plt.axis('scaled')
plt.show()