
import turtle 
import winsound

win_dows = turtle.Screen() 
win_dows.title("A Simple pong game")
win_dows.bgcolor("black")
win_dows.setup(width=800,height=600)
win_dows.tracer(0) # it helps the windows run fastest by stopping it from updating


#Score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle() # making it a turtule object
paddle_a.speed(0) # sets the object at the maximum speed
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=8,stretch_len=-1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle() # making it a turtule object
paddle_b.speed(0) # sets the object at the maximum speed
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=8,stretch_len=-1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle() # making it a turtule object
ball.speed(0) # sets the object at the maximum speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  PlayerB: 0", align="center", font= ("Courier", 24, "normal"))




# Functions

def paddle_a_up():
    y = paddle_a.ycor() # it returs the y cordinates
    y1 = y + 20 # adds 20 to the ycordinates to make a new one
    paddle_a.sety(y1)

def paddle_a_down():
    x = paddle_a.ycor() # it returs the y cordinates
    x1 = x - 20 # adds 20 to the ycordinates to make a new one
    paddle_a.sety(x1)

def paddle_b_up():
    y = paddle_b.ycor() # it returs the y cordinates
    y1 = y + 20 # adds 20 to the ycordinates to make a new one
    paddle_b.sety(y1)

def paddle_b_down():
    x = paddle_b.ycor() # it returs the y cordinates
    x1 = x - 20 # adds 20 to the ycordinates to make a new one
    paddle_b.sety(x1)

# Keyboard binging

win_dows.listen() # it listings for keyboard inputs 
win_dows.onkeypress(paddle_a_up,"w")

win_dows.listen() # it listings for keyboard inputs 
win_dows.onkeypress(paddle_a_down,"s")

win_dows.listen() # it listings for keyboard inputs 
win_dows.onkeypress(paddle_b_up,"Up")

win_dows.listen() # it listings for keyboard inputs 
win_dows.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    win_dows.update()
     
     # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # is used to play the sound in the background

    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(score_a,score_b), align="center", font= ("Courier", 24, "normal"))

        
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # is used to play the sound in the background


    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(score_a,score_b), align="center", font= ("Courier", 24, "normal"))


    # Paddle and ball collision 

    if (ball.xcor() > 340 and ball.xcor() < 350 ) and  (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        
    elif (ball.xcor() < -340 and ball.xcor() > -350 ) and  (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
   