"""A DevOps infinity-loop infographic drawn with turtle graphics."""

import math
import turtle


DARK_BG = "#11161d"
WHITE = "#f7f7f7"
GREEN = "#00d45a"

screen = turtle.Screen()
screen.setup(width=760, height=520)
screen.bgcolor(DARK_BG)
screen.title("DevOps Infinity Loop")
screen.tracer(0, 0)

pen = turtle.Turtle(visible=False)
pen.speed(0)


def polygon(points, color):
    """Draw a filled polygon from a list of (x, y) points."""
    pen.color(color)
    pen.fillcolor(color)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def arc(cx, cy, radius, start, end, color, width=52):
    """Draw a thick circular arc using standard counter-clockwise angles."""
    pen.color(color)
    pen.width(width)
    pen.penup()
    for degree in range(start, end + 1, 2):
        x = cx + radius * math.cos(math.radians(degree))
        y = cy + radius * math.sin(math.radians(degree))
        if degree == start:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    pen.penup()


def ribbon(start, end, half_width, color):
    """Draw the broad diagonal band crossing the two loops."""
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    nx, ny = -(ey - sy) / length * half_width, (ex - sx) / length * half_width
    polygon(
        [(sx + nx, sy + ny), (ex + nx, ey + ny),
         (ex - nx, ey - ny), (sx - nx, sy - ny)],
        color,
    )


def arrow_tip(x, y, direction, color, size=40):
    """Add a triangular arrow head pointing along ``direction`` degrees."""
    angle = math.radians(direction)
    back_x = x - math.cos(angle) * size
    back_y = y - math.sin(angle) * size
    side = size * 0.62
    left = (back_x + math.cos(angle + math.pi / 2) * side,
            back_y + math.sin(angle + math.pi / 2) * side)
    right = (back_x + math.cos(angle - math.pi / 2) * side,
             back_y + math.sin(angle - math.pi / 2) * side)
    polygon([(x, y), left, right], color)


# Separated arcs and arrowheads make each side read as a delivery cycle.
LEFT_X, RIGHT_X, CENTER_Y, RADIUS = -145, 145, 0, 108
arc(LEFT_X, CENTER_Y, RADIUS, 36, 146, WHITE)
arc(LEFT_X, CENTER_Y, RADIUS, 156, 278, WHITE)
arrow_tip(-57, 65, 17, WHITE, 31)
arrow_tip(-150, -108, 191, WHITE, 31)

arc(RIGHT_X, CENTER_Y, RADIUS, -34, 88, GREEN)
arc(RIGHT_X, CENTER_Y, RADIUS, 98, 218, GREEN)
arrow_tip(237, 65, 17, GREEN, 31)
arrow_tip(150, -108, 191, GREEN, 31)

# Draw the crossing last so the green path travels over the white loop.
ribbon((-80, -105), (85, 105), 29, GREEN)

# Dark masks form the clean gaps between the directional sections.
polygon([(-36, 48), (2, 48), (25, 23), (-11, 23)], DARK_BG)
polygon([(35, -48), (-3, -48), (-26, -23), (10, -23)], DARK_BG)

pen.color(GREEN)
pen.penup()
pen.goto(-145, -17)
pen.write("Dev", align="center", font=("Arial", 46, "bold"))
pen.color(WHITE)
pen.goto(145, -17)
pen.write("Ops", align="center", font=("Arial", 46, "bold"))

screen.update()
turtle.done()
