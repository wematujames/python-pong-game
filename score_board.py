from turtle import Turtle

TEXT_ALIGMENT = "center"
FONT = ("Courier", 16, "normal")
SCOREBOARDX = 0
SCOREBOARDY = 260


class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.create_scoreboard()
        self.update_score(0,0)
        
    #init scoreboard
    def create_scoreboard (self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCOREBOARDX, SCOREBOARDY)
    
    # On game over, display game over message
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=TEXT_ALIGMENT, font=FONT)
    
    #update score
    def update_score(self, p1_score, p2_score):
       self.clear()
       self.write(f"P1 Score: {p1_score} P2 Score: {p2_score}", align=TEXT_ALIGMENT, font=FONT)    
