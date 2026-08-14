import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
angle = 0

#screen.tracer(0)

while True:
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.color(colors[int(angle / 10) % len(colors)])
    for _ in range(4):
        t.forward(100)
        t.right(90)
    angle += 5
    screen.update()