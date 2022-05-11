#import pi value 
from math import pi
#make a function for total area 
def total_area(ball,area=0):
    #condition for min radius 
    if ball <2:
        #print the total area 
        print("The total surface area of chocolate was: {} mm^2 ".format(round(area,2)))
    else:
        #print the surface area and radius 
        print("Surface area of a chocolate ball with radius {} mm is {}.".format(ball,round(4*pi*ball*ball,2)))
        #calculate the total area 
        area =4*pi*ball*ball +area
        #call function 
        return total_area(ball-2,area)
        
#main method for test the function and ask the user for input 
if __name__ == '__main__':   
    ball = int(input("Enter the radius of the outer chocolate ball: "))
    total_area(ball)
