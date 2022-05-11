import turtle
number=int(input("How many polygons would you like to draw?"))

radius=int(input("What do you want the radius to increase by?"))

sides=int(input("How many sides do you wish to have?"))

clr=input("What color is the ring?")

t = turtle.Turtle()
size=30

angle=360/sides


t.setposition(0,0)


t.right(180)


def draw_polygon(size):

    t.color(clr)

    for i in range(sides):

        t.forward(size)

        t.left(angle)


for i in range(number):
    t.penup()

    t.right(90)

    t.forward(10)

    t.left(90)

    size=size + radius
    
    t.setposition(0,0)


    t.right(180)
    draw_polygon(size)

     

    t.pendown()