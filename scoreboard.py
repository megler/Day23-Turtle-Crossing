from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Create a scoreboard"""

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.color("Black")
        self.display_level()

    def display_level(self) -> None:
        """Display scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=(FONT))

    def level_up(self) -> None:
        """Increment level up by 1 each time player successfully crosses the road"""
        self.level += 1
        self.display_level()
