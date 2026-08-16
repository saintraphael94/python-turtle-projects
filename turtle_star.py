import turtle
t = turtle.Turtle()

sc = turtle.Screen()

t.speed(0)


t.pu()
t.goto(-200,0)
t.pd()

t.color('red', 'yellow')
t.begin_fill()
for i in range(16):
    t.forward(400)
    t.left(168)
t.end_fill()

t.hideturtle()
turtle.done()