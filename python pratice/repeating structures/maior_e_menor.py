# exercicio para descobrir o maior e o menor valor digitado

auxiliar1 = 0
auxiliar2 = 10**1000000 #alternativa para sair nao dar erro no auxiliar2

for i in range(1,11):
    numero = int(input(f"Digite o {i}- valor inteiro: "))
    if numero >= auxiliar1:
       maior_valor = numero
       auxiliar1 = numero
    else: 
        if numero < auxiliar2:
          menor_valor = numero
          auxiliar2 = numero
    

print(f"o maior numero digitado foi {maior_valor}")
print(f"o menor numero digitado foi {menor_valor}")
