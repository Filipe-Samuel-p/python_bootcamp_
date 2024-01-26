import random
from boneco import estagios


# VARIAVEIS
lista_de_palavras = ["computador", "engenharia", "software", "ciencia", "faculdade"]
palavra_escolhida = random.choice(lista_de_palavras) #escolhendo uma das palavras da lista
comprimento = len(palavra_escolhida)
tracos = []
vidas = 7
fim_do_jogo = False

# CRIANDO OS TRAÇOS 
for i in range(comprimento):
    tracos += "_"
 
while not fim_do_jogo:
    
    lista_preenchida = False
    letra_escolhida_pelo_usuario = input("Digite uma letra: ").lower()   #Existe diferença entre letras maiúsculas e minúsculas
    
    for i in range(comprimento): # o for irá percorrer cada letra!!
        if letra_escolhida_pelo_usuario == palavra_escolhida[i]:
            tracos[i] = letra_escolhida_pelo_usuario
    

    if letra_escolhida_pelo_usuario not in palavra_escolhida:
        vidas -= 1
        if vidas == 0:
            fim_do_jogo = True
            print(estagios[0])
            print("GAME OVER,YOU LOOSE!!!")
        else:
            print(estagios[vidas])

    win = "".join(tracos)
    print(win)

    if "_" not in tracos:
        fim_do_jogo = True
        print("Voce venceu!!!")
       
