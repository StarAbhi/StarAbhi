import math
#constant value 
pi=22/7
g=9.8
#take input from user 
cartMass=int(input("Enter the mass of the cart (in kg) : "))
pushForce=int(input("Enter the force to push the cart (in N) : "))
#calculate the angle in radian 
#here we use math.asin() function 
radianAngle=math.asin(pushForce/(cartMass*g))
#Now convert radian to degree 
degreeAngle=radianAngle*(180/pi)
#print the result value  at one decimal point by using round(value,no of digits) function 
print("The angle of the ramp is ",round(degreeAngle,1)," degrees")
