'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import GraphWin, Circle, Point, Line, Oval, Text


def main():
    win = GraphWin('Face', 200, 150)  # give title and dimensions
    win.setCoords(0, 0, 199, 149)

    head = Circle(Point(40,100), 25)  # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105))  # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))  # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()