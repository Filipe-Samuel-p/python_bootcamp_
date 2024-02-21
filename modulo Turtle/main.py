from turtle import *
import random


def cores_aleatorias():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   random_color = (r,g,b) 
   return random_color

colormode(255) #ver secao sobre cor em "pencolor" na documentação. Usa- se RGB
timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(15) #pensize aumenta a expessura da caneta da turtle
timmy_the_turtle.speed(3)
direcoes = [0,90,180,270]

for i in range(200):
   timmy_the_turtle.color(cores_aleatorias())
   timmy_the_turtle.forward(30)
   timmy_the_turtle.setheading(random.choice(direcoes)) #setheading escolhe aleatoriamente o a direcao da turtle, dai nao precisa usar os metodos right e left
  






exitonclick()






