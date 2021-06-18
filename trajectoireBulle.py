'''
This is the odc1nd changement 
'''

import numpy as np
import matplotlib.pyplot as plt


#trajectoire desirée
#Airlift de diamètre d et hauteur h
d = 0.8 # m
h = 2 # m
t = np.linspace(0, 3, 1000) # s

v0y = 0.5 # vitesse des bulles m/s
x0 = d/2 # m
f0 = 1
xAmplitude = d/2 # pylint: disable=C0103
y = v0y * t
x = x0 + xAmplitude * np.sin( 2 * np.pi * f0 * t)
plt.plot( x, y )

plt.title("Fonction cosinus")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.close()
plt.show()
