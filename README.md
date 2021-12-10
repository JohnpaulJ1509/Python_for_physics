# Python_for_physics
Description of the program:
    This program is uses to calculate velocity, acceleration and time in two different ways.
Instructions:
    1. For the magnitude part of the program assign the value 0 to the variable this is to be calculated
       for example: If you want to find time from initialvelocity, finalvelocity and acceleration the while
                              providing the values assign 0 to time.
    2. To find the velocity, acceleration or position from an equation then before executing the program give the equation in the program code.

Formula used:
u=v-at
u-initial velocity
v-final velocity
a-acceleration
t-time

Finding velocity and acceleration using position equation
	The fundamental theorem of calculus is used here.
	The change in position is velocity (1st derivative), the change in velocity is acceleration (2nd dative of position and 1st derivative of velocity) and vice versa.
	The sympy is package is used to perform integration and differentiation.
