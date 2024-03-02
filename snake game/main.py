from turtle import *
import random

def movimento_w():
    snake.right(90)
    snake.forward(10)

def movimento_s():
    snake.right(90)
    snake.backward(10)
def movimento_():
    snake.forward(10)
def movimento_w():
    snake.forward(10)

posicao_de_x = random.randint(-330,331)
posicao_de_y = random.randint(-280,280)


title("SNAKE GAME")
setup(width= 700, height= 600)
bolinha = Turtle(shape="circle")
bolinha.speed(-1)
bolinha.color("white")
snake = Turtle(shape="square")
snake.color("white")
bgcolor("black")

listen()
onkey(key= "w", fun=movimento_w)
onkey(key= "s", fun=movimento_s)




exitonclick()