from turtle import *
import turtle
#take number of diamond from user 
n=int(input("Enter Number of Diamond you want to drow :- "))
#set the speed of drowing 
speed(5)
#initial value of width
b=50
#set screen color 
bgcolor('white')
#set drowing pen color 
color('white')
#go 50 forward from center 
forward(b)
#by using fro loop draw diamond according to user given input 
for i in range(n):
    color('black')
    right(135)
    #draw diamond 
    for i in range(4):
        forward(b)
        right(90)
    right(225)
    color('white')
    forward(50)
    b=b+70
n=input("------END------")
