#!/usr/bin/env python3
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()

screen.listen()
screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with ceiling.
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision paddle.
    if ball.distance(paddle) < 50 and ball.xcor() > -400:
        ball.bounce_y()

    # Detect when paddle misses.
    if ball.ycor() < -380:
        ball.reset_position()

screen.exitonclick()
