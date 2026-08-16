import turtle

screen = turtle.Screen()
screen.bgcolor("#C7CCA7")
screen.title("Draw with arrow keys — space to lift pen, c to clear")

t = turtle.Turtle()
t.color("#1D0D58")
t.shape("turtle")
t.pensize(2)
t.speed(0)

def go_up():
    t.setheading(90)
    t.forward(20)

def go_down():
    t.setheading(270)
    t.forward(20)

def go_left():
    t.setheading(180)
    t.forward(20)

def go_right():
    t.setheading(0)
    t.forward(20)

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

def clear_screen():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(toggle_pen, "space")
screen.onkey(clear_screen, "c")

turtle.done()