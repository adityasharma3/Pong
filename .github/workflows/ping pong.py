import turtle

#Start settings

p=turtle.Screen()
p.title("Pong by Aditya")
p.bgcolor("black")
p.setup(width = 1000 , height = 700 )
p.tracer(0)

#Adding game componenets

#left paddle

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.penup()
paddle_a.goto(-400 , 0)
paddle_a.shapesize( stretch_wid = 7 , stretch_len =.75)


#right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.penup()
paddle_b.goto( 400 , 0)
paddle_b.shapesize( stretch_wid = 7 , stretch_len =.75)


# ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto( 0 , 0 )
ball.dx = 1
ball.dy = 1

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto( 0 , 300 )
pen.write("Player 1: 0   Player 2:0 " , align = "center" , font =("Courier" ,24 ,"bold"))


#score
score_1 = 0
score_2 = 0

# Creating Functions
def paddle_a_UP():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_DOWN():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_DOWN():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_b_UP():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Keyboard bindings

p.listen()
p.onkeypress( paddle_a_UP , "w")

p.listen()
p.onkeypress( paddle_a_DOWN , "s")

p.listen()
p.onkeypress( paddle_b_DOWN , "Down")

p.listen()
p.onkeypress( paddle_b_UP , "Up")


#Game loop

while True:
    p.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )

    #Border checking
    if ball.ycor() > 330:
        ball.sety(330)
        ball.dy *= -1


    if ball.ycor() < -330:
        ball.sety(-330)
        ball.dy *= -1

    if ball.xcor() < -480:
        ball.setx(-480)
        ball.goto( 0 , 0 )
        score_2= score_2 + 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {} ".format(score_1 , score_2), align = "center" , font =("Courier" ,24 ,"bold"))


    if ball.xcor() > 480:
        ball.setx(480)
        ball.goto( 0 , 0 )
        score_1 = score_1 + 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {} ".format(score_1 , score_2), align = "center" , font =("Courier" ,24 ,"bold"))


#Paddle and ball collisions
    if (ball.xcor() >345 and ball.xcor() <350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:

        ball.setx(345)
        ball.dx *=-1

    if (ball.xcor() <-345 and ball.xcor() >-350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:

        ball.setx(-345)
        ball.dx *=-1
