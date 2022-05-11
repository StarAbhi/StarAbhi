from turtle import *
import turtle

speed(10)
colors=['yellow','blue','red','cyan','gray']
forward(10)
for i in range(5):
    
    color(colors[i])
    bgcolor('black')
    b=150
    
    
 
    while b>0:
        left(b)
        forward(b*2)
        b=b-1
    right(90*(i+1))
    forward(400)

n=input("Wait ------")