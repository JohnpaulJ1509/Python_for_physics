# -*- coding: utf-8 -*-
"""
@author: John Paul J
"""

""" 
The second equation of motion does not give any deatil about the final velocity, So using this equation
we can find the final velocity of the ginen particle given the initial velocity, distance travelled and acceleration. 
Using these equations we can interpaly between the the variable.

"""
#start program
import math

print("Numeriacl model for third equation of motion.")

num=int(input("1.Final velocity\n2.Acceleration\n3.Distance\n4.Initial velocity\n"))

distance = float(input(" Distance :"))
initialvelocity = float(input(" Initial velocity : "))                      
acceleration = float(input(" Acceleration : "))
finalvelocity = float(input(" Final velocity :"))

if (num == 1):
    finalvelocity=math.sqrt((2*acceleration*distance)+initialvelocity**2)
    print(" Final velocity =",finalvelocity)
elif (num == 2):
    acceleration=((finalvelocity**2)-(initialvelocity**2))/(2*distance)
    print(" Acceleration = ",acceleration)
elif (num == 3):
    distance=((finalvelocity**2)-(initialvelocity**2))/(2*acceleration)
    print(" Distance = ",distance)
elif (num == 4):
    initialvelocity=math.sqrt((2*acceleration*distance)-finalvelocity**2)
    print(" Initial velocity =",initialvelocity)

else:
    print("ERROR")
    
#End program    
    
    