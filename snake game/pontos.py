from turtle import *

class Pontuacao(Turtle): #herança
    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Pontuação: {self.pontos}",align="center",font=("Arial",25,"normal"))
        self.hideturtle()
        self.penup()
      
    def nova_pontuacao(self):
        self.pontos += 1
        self.clear()
        self.write(f"Pontuação: {self.pontos}",align="center",font=("Arial",25,"normal"))

