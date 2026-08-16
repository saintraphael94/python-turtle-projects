import turtle
import time

sc = turtle.Screen()
sc.title("Analog Clock")
sc.bgcolor("black")

clock = turtle.Turtle()
clock.hideturtle()

def draw_hand(angle, length, color, pensize, width=None):
    clock.color(color)
    clock.pensize(pensize)
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(90 - angle)
    clock.pendown()
    clock.forward(length)

def draw_clock():
    clock.clear()

    clock.color("#ffffff")
    clock.pensize(3)
    clock.circle(200)

    now = time.localtime()
    sec = now.tm_sec
    min_ = now.tm_min
    hour = now.tm_hour % 12

    sec_angle = sec * 6
    min_angle = min_ * 6 + sec * 0.1
    hour_angle = hour * 30 + min_ * 0.5

    draw_hand(sec_angle, 180, "red", 1)
    draw_hand(min_angle, 160, "blue", 3)
    draw_hand(hour_angle, 100, "green", 5)

    sc.ontimer(draw_clock, 1000)

draw_clock()
sc.mainloop()
