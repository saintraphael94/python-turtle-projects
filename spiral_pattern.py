import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(200):
    t.color(colors[i % len(colors)])
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
turtle.done()