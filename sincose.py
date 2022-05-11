import math
#function 
def ellipse(x,y):
    result = 5*math.cos(x) + 9*math.sin(y)
    return result
#define x y with value
x=0.25
y=0.25
#call function  and print result
print("5 cos({}) + 9 sin({}) = {}".format(x,y,ellipse(x,y)))
