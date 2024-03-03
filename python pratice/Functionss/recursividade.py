def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return 1
    else:
       fat = n * fatorial(n - 1) #recursividade 
       return fat 
           

numero = int(input("Digite um numero inteiro: "))
valor = fatorial(numero)
print(f"O valor do fatorial de {numero} é {valor}") 