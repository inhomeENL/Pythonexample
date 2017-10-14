import turtle

def turn_right():
    turtle.setheading(0)
    turtle.forward(10)

def turn_up():
    turtle.setheading(90)
    turtle.forward(10)

def turn_left():
    turtle.setheading(180)
    turtle.forward(10)

def turn_down():
    turtle.setheading(270)
    turtle.forward(10)

def blank():
    turtle.clear()

turtle.shape("turtle")
turtle.speed(0)
turtle.onkeypress(turn_right, "Right")
turtle.onkeypress(turn_left, "Left")
turtle.onkeypress(turn_up, "Up")
turtle.onkeypress(turn_down, "Down")
turtle.onkeypress(blank, "Escape")
turtle.listen()
turtle.mainloop()