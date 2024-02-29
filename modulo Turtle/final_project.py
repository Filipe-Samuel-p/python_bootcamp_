from turtle import *

def movimento():
    tim.forward(10)



tim = Turtle()

listen() # funcao que faz a tela "ouvir" um comando e executar algo
onkey(key="space", fun= movimento) # funcao que quando a tecla "espaco"(poderia ser outra) for acionada, uma funcao ira ser usada
                                   # no caso, essa funcao usada é a "movimento", que cuida do movimento da turtle











exitonclick()