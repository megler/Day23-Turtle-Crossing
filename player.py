from turtle import Turtle, Screen
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.screen = Screen()
        self.car = CarManager()
        self.score = Scoreboard()

    def move_up(self) -> None:
        """Method of how far forward to move turtle at a time"""
        self.fd(MOVE_DISTANCE)

    def move_turtle(self, u: str) -> None:
        """Event listener to move turtle forward"""
        self.screen.listen()
        # onkeypress = fun name and argument to pass for which button moves turtle (eg. "Up")
        self.screen.onkeypress(self.move_up, u)

    def reset_player(self) -> None:
        """If turtle reaches finish line, level up and reset"""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.score.level_up()
            self.car.speed_up()

    def game_over(self) -> None:
        """If turtle collides with car, game over"""
        self.goto(0, 0)
        self.write(
            f"GAME OVER", align="center", font=("Courier", 24, "normal")
        )
