from turtle import *
import random

corrida_acontecendo = False
cores = ["orange", "red", "green", "yellow", "blue", "purple"]
todas_tartatugas = []


setup(width=500,height=400)
aposta = textinput(title="Faça uma aposta", prompt="Qual tartaruga deve ganhar a corrida? escolha uma cor")


y = -100
for tartarugas in range(0,6): #criacao das tartarugas 
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.penup()
    nova_tartaruga.color(cores[tartarugas])
    nova_tartaruga.goto(x= -230, y= y)
    todas_tartatugas.append(nova_tartaruga)
    y += 40


if aposta in cores:
    corrida_acontecendo = True

while corrida_acontecendo:
   for turtle in todas_tartatugas:
        if turtle.xcor() > 230:
            corrida_acontecendo = False
            cor_vencedora = turtle.pencolor()
            if cor_vencedora == aposta:
                print(f"Parabens, Voce venceu!!! a cor vencedora foi {cor_vencedora} ")
                break
            else:
                print(f"Voce perdeu!!! a cor vencedora foi {cor_vencedora}")
        distancia = random.randint(0,10)
        turtle.forward(distancia)


exitonclick()