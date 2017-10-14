import turtle
import random

class Chaser(turtle.Turtle):
    def SetStart(self, UserLocX, UserLocY):
        self.penup()
        while 1:
            LocX = random.randint(-200,200)
            LocY = random.randint(-150,150)
            if (LocX - UserLocX)**2 + (LocY - UserLocY)**2 < 200**2:
                continue
            else:
                break
        self.goto(LocX, LocY)
        self.pendown()
    def go(self, UserLocation):
        if random.randint(0, 100) % 10 == 0:
            self.setheading(random.randint(0, 359))
            self.forward(12)
        else:
            self.setheading(self.towards(UserLocation))
            self.forward(12)
    def Distance(self, UserLocX, UserLocY):
        Distance = (UserLocX - self.xcor()) ** 2 + (UserLocY - self.ycor()) ** 2
        return Distance

Chaser1 = Chaser()
Chaser1.shape('arrow')
Chaser2 = Chaser()
Chaser2.shape('arrow')
User = turtle.Turtle()
User.shape('circle')
Survive = 0
#유저 움직이기
def turn_right():
    global Survive
    Survive = Survive + 1
    User.setheading(0)
    User.forward(10)
#유저 움직임 따라서 컴퓨터 욺직이기 + 랜덤 방황
    Chaser1.go(User.position())
    Chaser2.go(User.position())
#일정거리 이하면 따라잡힌거로 취급
    if Chaser1.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 1, Survived : %d" %Survive)
        User.screen.bye()
    if Chaser2.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 2, Survived : %d" %Survive)
        User.screen.bye()

def turn_up():
    global Survive
    Survive = Survive + 1
    User.setheading(90)
    User.forward(10)
    Chaser1.go(User.position())
    Chaser2.go(User.position())
    if Chaser1.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 1, Survived : %d" %Survive)
        User.screen.bye()
    if Chaser2.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 2, Survived : %d" %Survive)
        User.screen.bye()

def turn_left():
    global Survive
    Survive = Survive + 1
    User.setheading(180)
    User.forward(10)
    Chaser1.go(User.position())
    Chaser2.go(User.position())
    if Chaser1.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 1, Survived : %d" %Survive)
        User.screen.bye()
    if Chaser2.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 2, Survived : %d" %Survive)
        User.screen.bye()

def turn_down():
    global Survive
    Survive = Survive + 1
    User.setheading(270)
    User.forward(10)
    Chaser1.go(User.position())
    Chaser2.go(User.position())
    if Chaser1.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 1, Survived : %d" %Survive)
        User.screen.bye()
    if Chaser2.Distance(User.xcor(),User.ycor()) < 100:
        print("Dead by Chaser 2, Survived : %d" %Survive)
        User.screen.bye()

def blank():
    User.clear()

User.speed(0)
#유저와 컴퓨터 초기 위치설정
(USPx, USPy) = (random.randint(-200,200), random.randint(-150,150))
User.penup()
User.goto(USPx, USPy)
User.pendown()
Chaser1.SetStart(User.xcor(), User.ycor())
User.screen.onkeypress(turn_right, "Right")
User.screen.onkeypress(turn_left, "Left")
User.screen.onkeypress(turn_up, "Up")
User.screen.onkeypress(turn_down, "Down")
User.screen.onkeypress(blank, "Escape")
User.screen.listen()
User.screen.mainloop()
