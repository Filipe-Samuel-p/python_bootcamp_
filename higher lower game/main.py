from dados import data
from random import randint
import logo

indice = randint(0,49)
pontos = 0
while True:
    print(f"Compare A: {data[indice]["name"]},{data[indice]['description']}, from {data[indice]["country"]}")
    print(logo.vs)
    indice2 = randint(0,49)
    print(f"Compare B: {data[indice2]["name"]},{data[indice2]['description']}, from {data[indice2]["country"]}")
    if data[indice]["follower_count"] > data[indice2]["follower_count"]:
        pontos += 1
    else:
        ...

 
        