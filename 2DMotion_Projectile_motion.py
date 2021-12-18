# -*- coding: utf-8 -*-
"""
@author: John Paul J

DISCRIPTION
A projectile is any body that is given an initial velocity and then follows a 
path determined entirely by the effects of gravitational acceleration and air resistance. 
A batted baseball, a thrown football, a package dropped from an airplane, 
and a bullet shot from a rifle are all projectiles. The path followed by a projectile 
is called its trajectory.

The key to analyzing projectile motion is that we can treat the x- and y-coordinates 
separately. The x-component of acceleration is zero, and the y-component is constant and equal to 
(By definition, g is always positive; with our choice of coordinate directions, is negative.) 
So we can analyze projectile motion as a combination of horizontal motion with constant velocity 
and vertical motion with constant acceleration.

REFERENCE: University Physics
Textbook by Hugh D. Young


ANALIZE THE MODEL BY CHANGING THE INITIAL CONDITIONS
"""

import numpy as np
import matplotlib.pyplot as plt


# INITIAL CONDITIONS CAN BE CHANGED
M = 1.0          # Mass of projectile in kg
g = 9.8          # Acceleration due to gravity (m/s^2)
V = 80           # Initial velocity in m/s
ang = 60.0       # Angle of initial velocity in degrees
Cd = 0      # Drag coefficient
dt = 0.1         # time step in s

# You can check the variables by printing them out
print ("Initial velocity, Initial angle, Mass, Coff. of drag",V,ang,M,Cd)

# Set up the lists to store variables
# Initialize the velocity and position at t=0
t = [0]                         # list to keep track of time
vx = [V*np.cos(ang/180*np.pi)]  # list for velocity x and y components
vy = [V*np.sin(ang/180*np.pi)]
x = [0]                         # list for x and y position
y = [0]

# Drag force
drag=Cd*V**2                      

# Acceleration components
ax = [-(drag*np.cos(ang/180*np.pi))/M ]          
ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ]

## Leave this out for students to try
# We can choose to have better control of the time-step here
dt = 0.2

# Use Euler method to update variables
counter = 0
while (y[counter] >= 0):                   # Check that the last value of y is >= 0
    t.append(t[counter]+dt)                # increment by dt and add to the list of time 
      
    # Update velocity
    vx.append(vx[counter]+dt*ax[counter])  # Update the velocity
    vy.append(vy[counter]+dt*ay[counter])

    # Update position
    x.append(x[counter]+dt*vx[counter])    
    y.append(y[counter]+dt*vy[counter])    

    # With the new velocity calculate the drag force and update acceleration
    vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2)   # magnitude of velocity
    drag = Cd*vel**2                                   # drag force 
    ax.append(-(drag*np.cos(ang/180*np.pi))/M)     
    ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
    
    # Increment the counter by 1
    counter = counter +1

# Let's plot the trajectory
plt.plot(x,y,'ro', color="green")
plt.ylabel("y (m)")
plt.xlabel("x (m)")
   
# The last value of x should give the range of the projectile approximately.

print ("Range of projectile is {:3.1f} m".format(x[counter]))
#End of the program