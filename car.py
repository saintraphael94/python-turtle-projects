import turtle

t = turtle.Turtle()
t.speed(6)
t.pensize(2)

# Car body
t.penup()
t.goto(-100, 0)
t.pendown()
t.color("black", "red")
t.begin_fill()
for length in [200, 40, 200, 40]:
    t.forward(length)
    t.left(90)
t.end_fill()

# Cabin
t.penup()
t.goto(-50, 40)
t.pendown()
t.color("black", "lightblue")
t.begin_fill()
for length in [100, 40, 100, 40]:
    t.forward(length)
    t.left(90)
t.end_fill()

# Wheels
def draw_wheel(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

draw_wheel(-70, -15)
draw_wheel(60, -15)

t.hideturtle()
turtle.done()