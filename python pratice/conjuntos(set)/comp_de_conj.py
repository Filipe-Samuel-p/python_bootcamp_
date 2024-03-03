import random

def criacao_da_lista(x):
    lista_criada = set()
    for i in range(x + 1):
        lista_criada.add(random.randint(1,10))
    return lista_criada

def operacoes_entre_conjuntos(lista1,lista2):
    conjunto_A = lista1   
    conjunto_B = lista2 
    valores_em_comum = set()

    for i in conjunto_A:
        if i in conjunto_B:
         valores_em_comum.add(i)
    
    valores_pertencentes_apenasA = conjunto_A - conjunto_B
    valores_pertencentes_apenasB = conjunto_B - conjunto_A

    print(f"Os numeros comum entre as duas listas: {valores_em_comum}")
    print(f"Os numeros que pertencem apenas ao conjunto A: {valores_pertencentes_apenasA}")
    print(f"Os numeros que pertencem apenas ao conjunto B: {valores_pertencentes_apenasB}")
    


try: 
    tamanho_lista1 = int(input("Digite o tamanho da lista 1: "))
    tamanho_lista2 = int(input("Digite o tamanho da lista 2: "))
    x = criacao_da_lista(tamanho_lista1)
    y = criacao_da_lista(tamanho_lista2)
    print("***** LISTA 1 *****\n")
    print("\n", x)
    print("\n***** LISTA 2 *****\n")
    print(y,"\n")
    operacoes_entre_conjuntos(x,y)

except:
    print("ERRO")