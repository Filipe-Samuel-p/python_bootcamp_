from dados import data
from random import randint
import logo
import os



indice = randint(0,49)
pontos = 0
while True:
    os.system("clear")
    print(logo.logo)
    print(f"Sua potuaçao é {pontos}\n")
    print(f"Personalidade A: {data[indice]["name"]}, {data[indice]['description']}, from {data[indice]["country"]}")
    print(logo.vs)
    indice2 = randint(0,49)
    print(f"Personalidade B: {data[indice2]["name"]}, {data[indice2]['description']}, from {data[indice2]["country"]}\n")
    decisao = input("Voce escolhe 'A'ou 'B'? : ")
    decisao_e_verificacao_A = decisao.lower() == "a" and data[indice]["follower_count"] > data[indice2]["follower_count"]
    decisao_e_verificacao_B = decisao.lower() == "b" and data[indice]["follower_count"] < data[indice2]["follower_count"]
    if decisao_e_verificacao_A or decisao_e_verificacao_B:
       pontos += 1
       if decisao_e_verificacao_A:
        continue
       else:
          indice = indice2 
    else:
        os.system("clear")
        print('Voce perdeu!!!')
        print(f"Sua potuaçao é {pontos}")
        break



 
        