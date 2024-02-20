from turtle import *

def triangulo():
    for i in range(3):
        timmy_the_turtle.right(120)
        timmy_the_turtle.forward(100)
    
def quadrado():
   for i in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100) #forward é movimentar a tartaruga para a frente. e passa como argumento a distancia

def pentagono():
   for i in range(5):
      timmy_the_turtle.right(72)
      timmy_the_turtle.forward(100)

def hexagono():
   for i in range(6):
      timmy_the_turtle.right(60)
      timmy_the_turtle.forward(100)

def heptagono():
   for i in range(7):
      timmy_the_turtle.right(51.5)
      timmy_the_turtle.forward(100)

def octgono():
   for i in range(8):
      timmy_the_turtle.right(45)
      timmy_the_turtle.forward(100)
   
def nonagon():
   for i in range(9):
      timmy_the_turtle.right(40)
      timmy_the_turtle.forward(100)

def decagono():
   for i in range(10):
      timmy_the_turtle.right(36)
      timmy_the_turtle.forward(100)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")



triangulo()
quadrado()
pentagono()
hexagono()
heptagono()
octgono()
nonagon()
decagono()







exitonclick()






