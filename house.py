import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(2)

# House body (square)
t.color("black")
t.begin_fill()
t.color("black", "lightyellow")
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# Roof (triangle)
t.penup()
t.goto(0, 0)
t.pendown()
t.color("black", "brown")
t.begin_fill()
t.left(30)
t.forward(170)
t.left(120)
t.forward(170)
t.left(120)
t.forward(170)
t.end_fill()

# Door
t.penup()
t.goto(60, 0)
t.pendown()
t.setheading(90)
t.color("black", "saddlebrown")
t.begin_fill()
for i in range(2):
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
t.end_fill()

# Window
t.penup()
t.goto(20, 90)
t.pendown()
t.color("black", "skyblue")
t.begin_fill()
for i in range(4):
    t.forward(30)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0, 200)
t.write("My House", align="center", font=("Metropolis", 16, "bold"))
t.hideturtle()
turtle.done()