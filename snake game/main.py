from turtle import *
import time
from snake_lib import Cobra
from comida import Food
from pontos import Pontuacao



# TELA (screen)
title("SNAKE GAME")
setup(width= 700, height= 600)
bgcolor("black")
tracer(0)
write("Pontuação",True,align="center")


#cobra
snake = Cobra()
snake.criacao_da_cobra()
comida = Food()
pontos = Pontuacao()

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

    #colisao
    if snake.cobra[0].distance(comida) < 15:
        pontos.nova_pontuacao()
        comida.nova_posicao()

    #colisao com a borda
    verificacao_da_colisao = snake.cobra[0].xcor() > 340 or snake.cobra[0].xcor() < -340 or snake.cobra[0].ycor() > 280 or snake.cobra[0].ycor() < -280
    if verificacao_da_colisao:
        color("white")
        write(f"GAME OVER ",align="center",font=("Arial",25,"normal"))
        break



exitonclick()