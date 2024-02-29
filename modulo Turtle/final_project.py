from turtle import *
import os

def movimento_W():
    tim.forward(10)

def movimento_para_tras():
    tim.backward(10)

def movimento_direita():
    tim.right(30)

def movimento_esquerda():
    tim.left(30)

def limpeza():
    os.system("clear")
    tim.home()


tim = Turtle()

listen() # funcao que faz a tela "ouvir" um comando e executar algo
onkey(key="w", fun= movimento_W) # funcao que quando a tecla "espaco"(poderia ser outra) for acionada, uma funcao ira ser usada
                                   # no caso, essa funcao usada é a "movimento", que cuida do movimento da turtle
onkey(key="s", fun= movimento_para_tras)
onkey(key="d", fun= movimento_direita)
onkey(key="a", fun= movimento_esquerda)
onkey(key="c", fun= limpeza)










exitonclick()