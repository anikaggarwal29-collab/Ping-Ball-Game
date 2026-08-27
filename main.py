import turtle

# Screen
screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score
score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0    Player B: 0",
            align="center", font=("Arial", 20, "normal"))


# Paddle movement
def left_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)


def left_down():
    y = left_paddle.ycor()
    if y > -250:
        left_paddle.sety(y - 20)


def right_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)


def right_down():
    y = right_paddle.ycor()
    if y > -250:
        right_paddle.sety(y - 20)


# Keyboard controls
screen.listen()

screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")

screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")


# Game loop
while True:
    screen.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.75

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.75

    # Right side collision
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -0.75
        score_a += 1

        score.clear()
        score.write(
            f"Player A: {score_a}    Player B: {score_b}",
            align="center",
            font=("Arial", 20, "normal")
        )

    # Left side collision
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -0.75
        score_b += 1

        score.clear()
        score.write(
            f"Player A: {score_a}    Player B: {score_b}",
            align="center",
            font=("Arial", 20, "normal")
        )

    # Paddle collision
    if (340 < ball.xcor() < 350 and
            right_paddle.ycor() - 50 < ball.ycor() <
            right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -0.75

    if (-350 < ball.xcor() < -340 and
            left_paddle.ycor() - 50 < ball.ycor() <
            left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -0.75