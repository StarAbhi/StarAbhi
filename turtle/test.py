import turtle

# create a turtle named t
t = turtle.Turtle()

# set up background color, pensize and speed
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(0)

# first loop: determines how many times the inner loop should be repeated
for i in range(8):
  # loop over each color in the list of available colors
  for j, color in enumerate(["red", "magenta", "blue", "cyan", "green", "yellow", "white"]):
    t.pencolor(color)
    if j % 2: # if j is odd, draw a circle with radius 100 
      t.circle(100)
    else: # if j is even, draw a circle with radius 50
      t.circle(50)
    t.left(10)

t.hideturtle()

