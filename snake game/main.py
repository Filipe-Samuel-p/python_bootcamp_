from turtle import *
import random

# TELA (screen)
title("SNAKE GAME")
setup(width= 700, height= 600)
bgcolor("black")


posicao_de_x = random.randint(-330,331)
posicao_de_y = random.randint(-280,280)


x=0
y=0
cobra = []
jogo_funcionando = True
for i in range(4):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x,y=y)
    x -= 10
    cobra.append(snake)


while jogo_funcionando:
    ...




exitonclick()