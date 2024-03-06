from turtle import *
import random

class Food(Turtle): #usando herança
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.nova_posicao()

    def nova_posicao(self):
       posicao_x = random.randint(-330,331)
       posicao_y = random.randint(-280,281)
       self.goto(posicao_x,posicao_y)