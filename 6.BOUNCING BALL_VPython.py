"""John Paul J
BOUNCING BALL SIMULATION
"""
from vpython import* 

scene = canvas(align="left")
scene.width = 250
scene.height = 450

scene.title = """The Size is not for scale. 
BOUNCING BALL SIMULATION"""

def display_instructions():
  s = """
              To rotate "camera", drag with right button or Ctrl-drag.
              To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.On a two-button mouse, middle is left + right.
              To pan left/right and up/down, Shift-drag.

              The plot is not for measurement.
              The plot gives only a graphical understanding of the bouncing ball. 

              REFERSH THE OUTPUT CONSOLE AFTER EACH EXECUTION
              
              
              
"""
  scene.caption = s

# Display text below the 3D graphics:
display_instructions()

# maximum graph range (integration time?)
tmax = 15   #time to plot the graph, can be changed accordingly
graphpos = True
graphvel = True
grapherg = True

# physics constants
cres = 0.9  #Coff. of restitution https://en.wikipedia.org/wiki/Coefficient_of_restitution
g = vec(0,-1,0) # natural units 
m = 1   #mass of the ball

# ground for collisions
h0 = vec(0,-0.5,0)
ground = box(pos=h0, size=0.4*vec(1,0.1,1), color=color.magenta, opacity=0.7)

# body
h = h0+vec(0,1,0)
v = vec(0,0,0)     # Initial velocity (0,<variable>9)
a = sphere(pos=h, radius=0.04, color=color.white, opacity=1)

# graphs or graphic curve
if graphpos:
  g1 = graph(scroll=True,align="right",width=400,height=150,ytitle="position",xmin=0,xmax=tmax,xtitle="time",title='Height against time')
  f1 = gcurve(graph=g1, interval=10, color=color.orange) 
if graphvel:
  g2 = graph(scroll=True,align="right",width=400,height=150,ytitle="velocity",xmin=0,xmax=tmax,xtitle="time",title='Velocity against time')
  f2 = gcurve(graph=g2, interval=10, color=color.cyan)
if grapherg:
  g3 = graph(scroll=True,align="right",width=400,height=250,xtitle="time",ytitle="energy",xmin=0,xmax=tmax,title='Energy against time')
  fp3 = gcurve(graph=g3, interval=10, color=color.red, label="PE") 
  fk3 = gcurve(graph=g3, interval=10, color=color.blue, label="KE") 
  ft3 = gcurve(graph=g3, interval=10, color=color.black, label="Total") 
t = 0
dt = 0.001
#Updating height and velocity
while t < tmax: 
#while True:
  rate(1/dt)
  v += g*dt
  h += v*dt
  a.pos = h
  
  # collisions of block a with ground
  if a.pos.y < ground.pos.y:
    v = cres*vec(0,mag(v),0)  #Calculating the velocity of the ball after collision
  
  # graphs
  t += dt
  
  if graphpos:
    f1.plot(data=[t,h.y-ground.pos.y]) 
  if graphvel:
    f2.plot(data=[t,v.y])
  
  pe = m*(-g.y)*(h.y-ground.pos.y)
  ke = 0.5*m*v.y*v.y
  
  if grapherg:
    fp3.plot(data=[t,pe])
    fk3.plot(data=[t,ke])
    ft3.plot(data=[t,pe+ke])
    
# label the parameters
print("Coff. of restution")
print(cres)

