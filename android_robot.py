"""
Draws the classic green Android robot mascot using the turtle module.
Run with: python3 draw_android_turtle.py
"""
import math
import turtle

GREEN = "#78C257"


def circle_points(cx, cy, r, start_deg, end_deg, steps=40):
    """Points along a circular arc from start_deg to end_deg (standard math angles)."""
    pts = []
    for i in range(steps + 1):
        ang = math.radians(start_deg + (end_deg - start_deg) * i / steps)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def fill_polygon(t, points):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.end_fill()


def draw_dome(t, cx, cy, r):
    """Upper half of a circle: flat bottom, rounded top (the head)."""
    pts = circle_points(cx, cy, r, 0, 180)  # right point -> top -> left point
    fill_polygon(t, pts)  # straight edge closes the flat bottom


def draw_capsule(t, cx, cy, width, height):
    """Vertical rounded-end capsule, centered at (cx, cy) — used for arms/legs."""
    r = width / 2
    top_cy = cy + height / 2 - r
    bottom_cy = cy - height / 2 + r
    top_arc = circle_points(cx, top_cy, r, 0, 180)
    bottom_arc = circle_points(cx, bottom_cy, r, 180, 360)
    fill_polygon(t, top_arc + bottom_arc)


def draw_rounded_rect(t, cx, cy, width, height, r):
    """Rounded rectangle centered at (cx, cy) — used for the body."""
    tr = circle_points(cx + width / 2 - r, cy + height / 2 - r, r, 0, 90)
    tl = circle_points(cx - width / 2 + r, cy + height / 2 - r, r, 90, 180)
    bl = circle_points(cx - width / 2 + r, cy - height / 2 + r, r, 180, 270)
    br = circle_points(cx + width / 2 - r, cy - height / 2 + r, r, 270, 360)
    fill_polygon(t, tr + tl + bl + br)


def draw_eye(t, cx, cy, r):
    pts = circle_points(cx, cy, r, 0, 360)
    t.fillcolor("white")
    fill_polygon(t, pts)
    t.fillcolor(GREEN)


def draw_antenna(t, base_x, base_y, tip_x, tip_y):
    t.penup()
    t.goto(base_x, base_y)
    t.pendown()
    t.pensize(6)
    t.goto(tip_x, tip_y)
    t.pensize(1)


def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.bgcolor("#E8F5E9")
    screen.title("Android Robot - Turtle Graphics")
    screen.tracer(0)  # draw instantly, then update once at the end

    t = turtle.Turtle()
    t.hideturtle()
    t.color(GREEN)

    # Antennae (draw first so the head/body cover only what they should)
    draw_antenna(t, -40, 150, -60, 210)
    draw_antenna(t, 40, 150, 60, 210)

    # Head (dome)
    draw_dome(t, 0, 60, 90)

    # Eyes
    draw_eye(t, -30, 100, 8)
    draw_eye(t, 30, 100, 8)

    # Body
    draw_rounded_rect(t, 0, -30, 180, 160, 20)

    # Arms
    draw_capsule(t, -125, -10, 35, 110)
    draw_capsule(t, 125, -10, 35, 110)

    # Legs
    draw_capsule(t, -40, -155, 35, 100)
    draw_capsule(t, 40, -155, 35, 100)

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()