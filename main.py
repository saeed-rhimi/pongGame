from turtle import Turtle, Screen
import scoreboard
import playground
import paddle
import ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = scoreboard.Scoreboard()
playground = playground.Playground()

right_paddle = paddle.Paddle((475, 0))
left_paddle = paddle.Paddle((-485, 0))

ball = ball.Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.01)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -280:
        ball.bounce_from_wall()

    if (ball.xcor() > 465 and ball.distance(right_paddle) < 60) or (
            ball.xcor() < -475 and ball.distance(left_paddle) < 60):
        ball.bounce_from_paddle()

    if ball.xcor() > 500 or ball.xcor() < -500:
        scoreboard.score_up(ball.xcor())
        scoreboard.update_scoreboard()
        ball.reset_ball()
        screen.update()
        time.sleep(1)


