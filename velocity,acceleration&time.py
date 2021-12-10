
"""
@author: J John Paul 
"""
"""
Description of the program:
    This program is uses to calculate velocity, acceleration and time in two different ways.
Instructions:
    1. For the magnitude part of the program assign the value 0 to the variable this is to be calculated
       for example: If you want to find time from initialvelocity, finalvelocity and acceleration the while
                    providing the values assign 0 to time.
    2. To find the velocity, acceleration or position from an equation then before executing the programm give the equation in the program code.

"""       
# Importing library
import sympy as sym

num = int(input(" For magnitude type enter 1.\n For calculus type entre 0.\n"))

if (num == 1):
    initialvelocity = int(input(" Initial velocity :"))
    finalvelocity = int(input(" Final velocity : "))                      
    acceleration = int(input(" Acceleration : "))           
    time = int(input(" Time : "))                     
    num1 = int(input(" what do you whant to find\n1.initial velocity\n2.final velocity\n3.acceleration\n4.time\n\t"))
    if num1 == 1:
           initialvelocity = finalvelocity - acceleration * time
           print("Initial velocity = ", initialvelocity)
    elif num1 == 2:
           finalvelocity = initialvelocity + acceleration * time
           print("Final velocity = ", finalvelocity)
    elif num1 == 3:
           acceleration = (finalvelocity - initialvelocity) / time
           print("Acceleration = ", acceleration)
    elif num1 == 4:
           time = (finalvelocity - initialvelocity) / acceleration
           print("Time taken = ", time)
else:
    t = sym.symbols('t')
    x = 5*t**3 + 2*t + 8       #EXPRESSION TO BE EVALUATED
    num2 = int(input("1.To find velocity and acceleration from position \n2.To find position and veloctiy from acceleration \n3.To find positon and acceleration fron velocity\n\t"))
    if num2 == 1:
        velocity = sym.diff(x, t)
        print('Veloctiy: ',velocity)
        acceleration = sym.diff(velocity, t,)
        print('Acceleration :',acceleration)
    elif num2 == 2:
        velocity = sym.integrate(x, t)
        position = sym.integrate(velocity, t)
        print('Position :',position)
        print('Velocity :',velocity)
    elif num2 == 3:
        position = sym.integrate(x, t)
        print('Position :',position)
        acceleration = sym.diff(x,t)
        print('Acceleration :',acceleration) 
      
#end of the program   
