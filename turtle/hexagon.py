from turtle import *
import turtle
#function for  Hexagon 
def drawHexagon():
    for i in range(6):
        forward(90)
        left(300)
#loop to draw 7 hexagon in honeycomb pattern.
color('white')
forward(50)
left(220)
#loop for to drow 7 hexagon
for i in range(7):
    color('white')
    forward(180)
    color('black')
    drawHexagon()
    right(60)
    
Stop=input()