# exercicio da soma de fatoriais 
 
# soma : E(n) = 1 + 1/1! + 1/2! + 1/3!...1/n! 

def fatorial (n):
    fat = 1
    for valor in range(1, n+1):
        fat *= valor
    return fat


n1 = int(input("Digite um valor: "))
soma = 1
for i in range(1, n1+1):
    soma += 1/fatorial(i)
print(f"O valor da soma é {soma} ") 