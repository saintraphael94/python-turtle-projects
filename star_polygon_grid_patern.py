import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(1)

def star(size, color_):
    t.color(color_)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

colors = ["gold", "orange", "crimson", "purple", "royalblue"]
t.penup()

for row in range(4):
    for col in range(4):
        t.goto(-180 + col * 120, -180 + row * 120)
        t.pendown()
        star(50, colors[(row + col) % len(colors)])
        t.penup()

t.hideturtle()
turtle.done()