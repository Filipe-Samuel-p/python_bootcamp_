from turtle import *
import random

def cores_aleatorias():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   random_color = (r,g,b) 
   return random_color


colormode(255)
timmy = Turtle()
timmy.speed(10.5)

for i in range(100):
    timmy.color(cores_aleatorias())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)




exitonclick()