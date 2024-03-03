from turtle import *

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Cobra():

    def __init__(self) -> None:
        self.cobra = []
        self.criacao_da_cobra
        
        
    def criacao_da_cobra(self):
        x=0
        y=0
        for i in range(4):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=x,y=y)
            x -= 10
            self.cobra.append(snake)

    def movimento_da_cobra(self):
        for i in range(len(self.cobra)-1,0,-1):
            novo_x = self.cobra[i-1].xcor()
            novo_y = self.cobra[i-1].ycor()
            self.cobra[i].goto(novo_x,novo_y)
        self.cobra[0].forward(20)

    def snake_up(self):
        if self.cobra[0].heading() != DOWN:
            self.cobra[0].setheading(UP)

    def snake_left(self):
        if self.cobra[0].heading() != RIGHT:
            self.cobra[0].setheading(LEFT)
   
    def snake_right(self):
        if self.cobra[0].heading() != LEFT:
            self.cobra[0].setheading(RIGHT)
   
    def snake_down(self):
        if self.cobra[0].heading() != UP:
            self.cobra[0].setheading(DOWN)
