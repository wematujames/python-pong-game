from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
from turtle import Screen
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Set up screen 
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

#Init score score_board
scoreboard = Scoreboard()

#Init Pong ball
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

# Init Player 1
player1 = Paddle("p1", SCREEN_WIDTH, SCREEN_HEIGHT)
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")

# Init Player 2
player2 = Paddle("p2", SCREEN_WIDTH, SCREEN_HEIGHT)
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")


# Main game loop
game_on = True
while game_on: 
    screen.update()
    time.sleep(ball.ball_speed_val)
    ball.move()
    
    # Detect collision with wall (bottom and top)
    if ball.ycor() > SCREEN_HEIGHT/2 - 15 or ball.ycor() < -SCREEN_HEIGHT/2 + 15:
        ball.bounce_y()
        
    #Detect collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() < -SCREEN_WIDTH/2 + 50 or ball.distance(player2) < 50 and ball.xcor() > SCREEN_WIDTH/2 - 50:
        ball.bounce_x()
    
    # Detect when player missed the ball
    if ball.xcor() < -SCREEN_WIDTH/2 - 20:
        player2.score += 1
        scoreboard.update_score(player1.score, player2.score)
        ball.reset()
    elif ball.xcor() > SCREEN_WIDTH/2 + 20:
        player1.score += 1
        scoreboard.update_score(player1.score, player2.score)
        ball.reset()

#Exit screen on click
screen.exitonclick()