import turtle
import time
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ClockConfig:
    title: str = "Analog Clock"
    bg_color: str = "black"
    face_color: str = "#ffffff"
    face_radius: int = 200
    face_pensize: int = 3
    tick_color: str = "white"
    number_color: str = "white"
    update_interval_ms: int = 1000

    HandSpec = Tuple[int, str, int]
    SECOND_HAND: "ClockConfig.HandSpec" = (180, "red", 1)
    MINUTE_HAND: "ClockConfig.HandSpec" = (160, "lime green", 3)
    HOUR_HAND: "ClockConfig.HandSpec" = (100, "blue", 5)

    hands: Tuple["ClockConfig.HandSpec", ...] = (
        SECOND_HAND,
        MINUTE_HAND,
        HOUR_HAND,
    )


class AnalogClock:
    def __init__(self, config: ClockConfig = ClockConfig()):
        self.config = config
        self.screen = turtle.Screen()
        self.screen.title(config.title)
        self.screen.bgcolor(config.bg_color)
        self.screen.tracer(0, 0)

        self._running = True

        # Static clock face (drawn once)
        self._face_turtle = turtle.Turtle()
        self._face_turtle.hideturtle()
        self._draw_static_face()

        self._hub_turtle = turtle.Turtle()
        self._hub_turtle.hideturtle()
        self._draw_hub()

        # One turtle per hand for efficient updates
        self._hand_turtles = []
        for length, color, pensize in config.hands:
            hand_turtle = turtle.Turtle()
            hand_turtle.hideturtle()
            hand_turtle.color(color)
            hand_turtle.pensize(pensize)
            self._hand_turtles.append(hand_turtle)

    def _draw_static_face(self) -> None:
        """Draw the centred clock outline, tick marks, and numerals once."""
        face = self._face_turtle
        radius = self.config.face_radius

        face.color(self.config.face_color)
        face.pensize(self.config.face_pensize)
        face.penup()
        face.goto(0, -radius)
        face.setheading(0)
        face.pendown()
        face.circle(radius)

        for mark in range(60):
            angle = mark * 6
            tick_length = 14 if mark % 5 == 0 else 6
            face.color(self.config.tick_color)
            face.pensize(2 if mark % 5 == 0 else 1)
            face.penup()
            face.goto(0, 0)
            face.setheading(90 - angle)
            face.forward(radius - 3)
            face.pendown()
            face.backward(tick_length)

        face.color(self.config.number_color)
        face.penup()
        for number in range(1, 13):
            angle = number * 30
            face.goto(0, 0)
            face.setheading(90 - angle)
            face.forward(radius - 28)
            face.write(str(number), align="center", font=("Arial", 16, "normal"))

    def _draw_hub(self) -> None:
        """Draw the small centre cap shown over the hands."""
        hub = self._hub_turtle
        hub.color("white")
        hub.penup()
        hub.goto(0, -7)
        hub.pendown()
        hub.pensize(2)
        hub.circle(7)

    @staticmethod
    def _position_hand(hand_turtle: turtle.Turtle, angle: float, length: int) -> None:
        """Move a hand turtle to the correct position and draw."""
        hand_turtle.clear()
        hand_turtle.penup()
        hand_turtle.goto(0, 0)
        hand_turtle.setheading(90 - angle)
        hand_turtle.pendown()
        hand_turtle.forward(length)

    def _get_hand_angles(self) -> Tuple[float, float, float]:
        """Calculate angles for the second, minute, and hour hands."""
        now = time.localtime()
        sec = now.tm_sec
        min_ = now.tm_min
        hour = now.tm_hour % 12

        return (
            sec * 6,
            min_ * 6 + sec * 0.1,
            hour * 30 + min_ * 0.5,
        )

    def _update(self) -> None:
        """Redraw hands and schedule the next update."""
        if not self._running:
            return

        try:
            angles = self._get_hand_angles()
            for hand_turtle, (length, _, _), angle in zip(
                self._hand_turtles, self.config.hands, angles
            ):
                self._position_hand(hand_turtle, angle, length)

            self._draw_hub()
            self.screen.update()
            self.screen.ontimer(self._update, self.config.update_interval_ms)
        except turtle.Terminator:
            self._running = False
        except Exception:
            self._running = False

    def run(self) -> None:
        """Start the clock."""
        self._update()
        self.screen.mainloop()


if __name__ == "__main__":
    AnalogClock().run()
