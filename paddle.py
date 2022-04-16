from turtle import Turtle

class Paddle(Turtle): 
    def __init__(self,player, screen_width, screen_height):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(player == "p1" and -screen_width/2 + 13 or screen_width/2 - 20, 0)
        self.screen_height = screen_height
        self.score = 0
        
    # Movement 
    def up(self):
        if self.ycor() < self.screen_height/2 - 50:
            self.goto(self.xcor(), self.ycor() + 20)
        
    def down(self):
        if self.ycor() > -self.screen_height/2 + 50:
            self.goto(self.xcor(), self.ycor() - 20)
        
        