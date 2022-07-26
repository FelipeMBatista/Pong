import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

def moves():
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()
    moves()
    time.sleep(ball.move_speed)
    ball.ball_movement()
    # Detectar bounce no teto
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detectar bounce no paddle
    if ball.distance(r_paddle.pos()) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle.pos()) < 50 and ball.xcor() < -320:
        ball.paddle_collision()
    # Detectar bola fora e reiniciar
    if ball.xcor() > 380:
        ball.out_of_bounds()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.out_of_bounds()
        scoreboard.r_point()

screen.exitonclick()