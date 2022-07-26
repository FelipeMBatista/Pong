from turtle import Turtle

DEFAULT_MOVE = 5
DEFAULT_SPEED = 0.06
SPEED_INCREASE = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.y_move = DEFAULT_MOVE
        self.x_move = DEFAULT_MOVE
        self.move_speed = DEFAULT_SPEED

    def ball_movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1
        self.move_speed *= SPEED_INCREASE

    def out_of_bounds(self):
        self.home()
        self.x_move *= -1
        self.move_speed = DEFAULT_SPEED