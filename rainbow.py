import turtle
pen = turtle.Turtle()
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("#140F0F")

def semi_circle(colors, radius, value):
    pen.color(colors)
    pen.circle(radius, -180)
    pen.penup()
    pen.setpos(value,0)
    pen.pendown()
    pen.right(180)
    
colors = ['red','green','blue', 'orange', 'indigo', 'violet', 'yellow']

pen.right(90)
pen.width(10)

for i in range(len(colors)):
    semi_circle(colors[i], 10*(i+8), -10*(i+1))

pen.hideturtle()
screen.exitonclick()
turtle.done()