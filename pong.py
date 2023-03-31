from gzip import _PaddedFile
import turtle

win = turtle.Screen()
win.title("pong from yt")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)
#score
score_a = 0
score_b = 0

#paddel 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("yellow")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#paddel 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
# function

def paddle_1_up():
    y=paddle_1.ycor()
    y+=20
    paddle_1.sety(y)

def paddle_1_down():
    y=paddle_1.ycor()
    y-=20
    paddle_1.sety(y)

def paddle_2_up():
    y=paddle_2.ycor()
    y+=20
    paddle_2.sety(y)

def paddle_2_down():
    y=paddle_2.ycor()
    y-=20
    paddle_2.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_1_up,"e")
win.onkeypress(paddle_1_down,"x")
win.onkeypress(paddle_2_up,"Up")
win.onkeypress(paddle_2_down,"Down")
#main game loop
while True:
    win.update()


    # moving of the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    # boarder checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
    # ppaddle and ball collitions
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor() < -340 and ball.xcor()>-350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx*=-1