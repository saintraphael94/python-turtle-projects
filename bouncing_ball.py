import turtle

screen = turtle.Screen()
screen.setup(500, 400)
screen.bgcolor("black")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)

dx, dy = 3, 2

while True:
    x, y = ball.xcor(), ball.ycor()
    if x > 240 or x < -240:
        dx *= -1
    if y > 190 or y < -190:
        dy *= -1
    ball.goto(x + dx, y + dy)