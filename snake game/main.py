from turtle import *
import random

posicao_de_x = random.randint(-330,331)
posicao_de_y = random.randint(-540,541)



setup(width= 700, height= 600)
bolinha = Turtle(shape="circle")
snake = Turtle(shape="square")
snake.color("white")
bgcolor("black")




exitonclick()