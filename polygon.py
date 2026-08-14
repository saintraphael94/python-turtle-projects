import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("#AAD8C6")
screen.title("Polygons")

t.pencolor("#091236")
t.pensize(3)
t.shape("circle")


t.penup()
t.goto(-150,-250)
t.pendown()

num_side = 9
pen_length = 100
angle = 360/num_side

t.color("#000000", "#D7B3D5")

t.begin_fill()
for i in range(num_side):
    t.forward(pen_length)
    t.left(angle)
t.end_fill()
        
t.hideturtle()

turtle.done()