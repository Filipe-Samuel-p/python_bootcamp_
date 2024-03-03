from turtle import *
import random
import time
from snake_lib import Cobra

def snake_up():
    setheading(0)



# TELA (screen)
title("SNAKE GAME")
setup(width= 700, height= 600)
bgcolor("black")
tracer(0)

#cobra
snake = Cobra()
snake.criacao_da_cobra()

# Teclas para movimentar a cobra
listen()
onkey(snake.snake_up,"Up")
onkey(snake.snake_down,"Down")
onkey(snake.snake_left,"Left")
onkey(snake.snake_right,"Right")


jogo_funcionando = True
while jogo_funcionando:
    update()
    time.sleep(0.1)
    snake.movimento_da_cobra()

    



exitonclick()