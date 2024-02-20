from turtle import *


def criacao_do_poligono(lados,angulos):
    for i in range(lados):
        timmy.right(angulos)
        timmy.forward(100) #forward é movimentar a tartaruga para a frente. e passa como argumento a distancia


timmy = Turtle()

numero_de_lados = list(range(3,11))
angulos = [120,90,72,60,51.42,45,40,36]

for j in range(8):
    criacao_do_poligono(numero_de_lados[j],angulos[j])



exitonclick()