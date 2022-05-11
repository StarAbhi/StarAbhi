from turtle import *
import turtle

speed(15)
colors=['yellow','blue','red','cyan','green','pink']
right(270)
forward(180)
bgcolor('black')
for i in colors:
    color(i)
    b=140
    while b>0:
        forward(b)
        right(b*2)
        b=b-1
n=input("Wait ------")