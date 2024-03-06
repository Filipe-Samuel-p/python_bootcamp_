from turtle import *
import random
import time
from snake_lib import Cobra
from comida import Food

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
comida = Food()

# Teclas para movimentar a cobra
listen()
onkey(snake.snake_up,"Up")
onkey(snake.snake_down,"Down")
onkey(snake.snake_left,"Left")
onkey(snake.snake_right,"Right")

pontuacao = 0
jogo_funcionando = True
while jogo_funcionando:
    update()
    time.sleep(0.1)
    snake.movimento_da_cobra()

    #colisao
    if snake.cobra[0].distance(comida) < 15:
        pontuacao += 1
        comida.nova_posicao()

    



exitonclick()