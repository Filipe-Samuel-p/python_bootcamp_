# *******  BUBLLE SORT ******

import random # metodo random 

def criacao_da_lista(n):
   global lista 
   for i in range(n):
     lista.append(random.randint(1,100))
   return lista


def bublle_Sort(n):
 temp = 0
 while True:
    trocou = False
    for i in range(n - 1): # n -1 equivale ao numero de comparacoes. Alem disso, impede que de um IndexError, por causa do tamanho da lista
        if lista[i] > lista[i + 1]:
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp
            trocou = True
    if not trocou:
        break

lista = []
numero = int(input('Digite o tamanho da lista: '))
criacao_da_lista(numero)
print("\n ***** LISTA ALEATORIA ******")
print(lista, "\n" )
bublle_Sort(numero)
print("***** LISTA ORDENADA ******")
print(lista, "\n") 