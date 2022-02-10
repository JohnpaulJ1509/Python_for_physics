import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#finding the velocity and acceleration
t = Symbol('t')
x = 5*t**3 + 2*t + 8   # EXPRESSION TO BE EVALUATED  
v=x.diff(t) # dx/dt
a = v.diff(t)# dv/dt
print(f"The positon is:",x)
print(f"The speed  is:",v)
print(f"The acceleration  is:",a)

#plotting it in graph
def func(t):
    return  5*t**3 + 2*t + 8    # EXPRESSION TO BE EVALUATED

xlist = np.linspace(-10,10)
ylist = func(xlist)

plt.figure(1,dpi=300)
plt.plot(xlist,ylist,label="Position", color ='r')

"""
Defining the first deravative naming it as D. We take in the xlist and ylist.
yprime is the derivative of the y values.It can be done using a simole difference formula.
np.diff() will Calculate the n-th discrete difference along the given axis.
del y/del x will give us the deravitive of the y.
If we want to find the deravitive bw two points we need to take it in the meiddel.
we use for loop in xprime because it will runn till yprime runs.
https://numpy.org/doc/stable/reference/generated/numpy.diff.html
"""  
def D(xlist,ylist):
    yprime = np.diff(ylist)/np.diff(xlist)
    xprime=[]
    for i in range(len(yprime)):
        xtemp = (xlist[i+1]+xlist[i])/2
        xprime = np.append(xprime,xtemp)
    return xprime, yprime

xprime, yprime = D(xlist,ylist)
plt.plot(xprime,yprime,label="Velocity", color ='g')

xprime2, yprime2 = D(xprime,yprime)
plt.plot(xprime2,yprime2,label="Acceleration", color ='b')

plt.xlabel('time')
plt.ylabel('x / v / a ')

plt.legend()
plt.grid(True)

