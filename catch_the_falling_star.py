import turtle
import random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Catch the Star!")
screen.tracer(0)

# Basket (player)
basket = turtle.Turtle()
basket.shape("square")
basket.color("white")
basket.shapesize(1, 5)
basket.penup()
basket.goto(0, -220)

# Star (falling object)
star = turtle.Turtle()
star.color("yellow")
star.shape("circle")
star.penup()
star.goto(random.randint(-230, 230), 220)

score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 230)
scoreboard.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))

def move_left():
    x = basket.xcor()
    basket.goto(max(x - 30, -230), -220)

def move_right():
    x = basket.xcor()
    basket.goto(min(x + 30, 230), -220)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

while True:
    star.sety(star.ycor() - 3)

    if star.ycor() < -200 and abs(star.xcor() - basket.xcor()) < 40:
        score += 1
        star.goto(random.randint(-230, 230), 220)
        scoreboard.clear()
        scoreboard.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))

    if star.ycor() < -240:
        star.goto(random.randint(-230, 230), 220)

    screen.update()