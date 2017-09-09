import turtle
import random

turtle = turtle.Turtle()
Diameter = int(input("Circle Diameter: "))
turtle.penup()
turtle.right(90)
turtle.forward(Diameter)
turtle.pendown()
turtle.left(90)
turtle.circle(Diameter)
turtle.penup()
turtle.home()
turtle.pendown()
TurtleEnd = 0
while 1:
    UserLength = int(input("Forward: "))
    turtle.forward(UserLength)
    Heading = random.randint(0, 360)
    turtle.right(Heading)
    (x, y) = turtle.position()
    if x*x + y*y > Diameter*Diameter:
        turtle.undo()
        turtle.undo()
        while 1:
            turtle.forward(1)
            (x, y) = turtle.position()
            if x*x + y*y > Diameter*Diameter:
                turtle.undo()
                TurtleEnd = 1
                break
    if TurtleEnd == 1:
        break

turtle.screen.mainloop()