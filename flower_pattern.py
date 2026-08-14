import turtle
t = turtle.Turtle()

s = turtle.Screen()
s.bgcolor("#BECFA7")


t.speed(0)
t.pensize(2)
t.shape("turtle")

colors = ["red", "purple", "blue", "green", "orange", "#000000"]

for i in range(36):
    t.color(colors[i % len(colors)])
    t.circle(80)
    t.left(25)

t.hideturtle()
turtle.done()