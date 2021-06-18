import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos


#trajectoire desirée
#Airlift de diamètre d et hauteur h
d = 0.8 # m
h = 2 # m

v0y = 0.5 # vitesse des bulles m/s
x0 = d/2 # m
x_0 = 2
f0 = 1
xAmplitude = d/2
T  = 0
dt = 0.1 # s

for i in range(10):
    t = np.linspace(0,T,100)
    y = v0y * t
    x = x0 + xAmplitude * np.sin( 2 * pi * f0 * t)

    plt.plot(x,  y)
    plt.xlim(0, d)
    plt.ylim(0, h)
    plt.grid()
    plt.pause(0.01) # pause avec duree en secondes
    T = T + dt
plt.show()


#
# y = v0y * t
# x = x0 + xAmplitude * np.sin( 2 * pi * f0 * t)
# plt.plot( x, y )
