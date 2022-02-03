"""
@author: John Paul J
"""

""" 
This program will be a numerical model fro the second equation of motion in general mechanics.
Using this one can find the distance or acceleration or the initial velocity if time and other variables are provided.
Give the value 0 to the unknown variable when one want to find it.
Using the program "1st eq of motion_velocity,acceleration and time" the concept of solving problem can be extended.
NOTE: This equation is not used to find the time.
"""
#start program

print("Numerical model of second equation of motion")

num = float(input("\n1. To find distance enter 1.\n2. To find initial velocity enter 2\n3. To find acceleration enter 3\n"))

distance = float(input(" Distance :"))
initialvelocity = float(input(" Initial velocity : "))                      
acceleration = float(input(" Acceleration : "))
time = float(input(" Time :"))

if (num == 1):
    distance=(initialvelocity*time)+(acceleration*time**2)/2
    print(" Distance = ",distance)
elif (num == 2):
    initialvelocity=(distance-((acceleration*time**2)/2))/time
    print(" Initial velocity = ",initialvelocity)
elif (num == 3):
    acceleration=((distance-initialvelocity*time)/(time**2))*2
    print("Acceleration = ",acceleration)
else:
    print("ERROR")
    
#End program    