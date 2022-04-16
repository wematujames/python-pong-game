from turtle import Turtle
import random

class Ball (Turtle):
    def __init__ (self, screen_width, screen_height):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.dx = random.randint(1, 3)
        self.dy = random.randint(1,3)
        self.move_x = 10
        self.move_y = 10
        self.ball_speed_val = 0.1
        
    def move (self):
            new_x = self.xcor() + self.move_x
            new_y = self.ycor() + self.move_y
            self.goto(new_x, new_y)
        
    def bounce_x (self): 
        self.move_x *= -1
        self.ball_speed_val = 0.05
        
    def bounce_y (self): 
        self.move_y *= -1
        self.ball_speed_val = 0.1
        
    def reset (self): 
        self.goto(0, 0)
        self.ball_speed_val = 0.1
            