from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.go_to_start()
        self.setheading(90)

    def turtle_moving(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def turtle_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



