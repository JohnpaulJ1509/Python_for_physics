
"""John Paul J
SIMPLE HARMONIC MOTION - SIMULATION (BASIC)
"""

from vpython import*

display(background=color.white)

totalTime=50 #in seconds
f1 = graph(xmin=0,xmax=totalTime,xtitle='<i>t</i> in seconds')
f1 = gdots(color=color.green, label='position',fast=True) #Potition graph


Mass = box(pos=vector(10,0,0),velocity=vector(0,0,0),color=color.red,mass=2) #Defining the mass
pivot = vector(-10,0,0)

spring = helix(pos=pivot,axis=Mass.pos-pivot,radius=0.5,coils=20,
               constant=(pi*pi)/4,thicnkess=0.1,color=color.orange) #Defining the spring using helix
eq = vector(0,0,0)

t = 0
dt = .005 #if time step is smaller than this, 
          #then completion time will not be the total time duration.

while (t <= totalTime):
    frameRate = 1/dt
    rate(frameRate)
    acc = (eq-Mass.pos)*(spring.constant/Mass.mass)
    Mass.velocity = Mass.velocity+acc*dt
    Mass.pos = Mass.pos+Mass.velocity*dt
    spring.axis = Mass.pos-spring.pos
    
    f1.plot(t,Mass.pos.x) #Plotting the graph
    t = t + dt 
    
# end program