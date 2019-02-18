# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 14:40:27 2019

@author: Kris
"""

#in this code, i will determine a x0, p0, and tehn use the arnold cat matrix to transforma  few thousand times
#then plot, see how the distrbution is

import matplotlib.pyplot as plt
import numpy as np


#define starting point
x0 = 0.25
p0 = 0.5
point = [x0, p0]
#arnold parameters/coefficients
a = 3
b = 1
c = 2

testx1 = a*x0 + b*p0
testp1 = c*x0 + b*p0
testx2 = (a*testx1 + b*testp1) %1

#define the transform
def arnold(point):
    pos = point[0]
    mom = point[1]
    posnew = (3*pos + 1*mom) % 1
    momnew = (2*pos + 1*mom) % 1

    newpoint = [posnew, momnew]
    return newpoint


#loop to get a bunch of values
n = 4000     #will eventually move up to 1000
allpoints = np.zeros((2, n))
pointloop = point           #initial conditions
for i in range (0,n):
    allpoints[:, i] = arnold(pointloop)
    allpoints[0,i] = round(allpoints[0,i],2)
    allpoints[1,i] = round(allpoints[1,i],2)
    pointloop = allpoints[:,i]


plt.plot(allpoints[0,:], allpoints[1,:], 'r.' )
plt.plot(point[0], point[1],'go',label= "orginial point")
plt.title("arnold transform for point {}".format(point))
plt.legend()
plt.xlabel("x")
plt.ylabel("p")