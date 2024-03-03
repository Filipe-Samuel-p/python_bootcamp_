# FATORIAL 

# MODO 1 

def fatorial(x):
    fat = 1
    c = 1
    while c <= x:
        fat *= c
        c += 1
        
    return fat

n1 = int(input("Digite um valor: "))
print(f"o fatorial de {n1} é {fatorial(n1)}")

# MODO 2

def fatorial(n):
    fat = 1
    for valor in range(1,n +1):
        fat = fat * valor
    return fat


n1 = int(input("Digite um valor: "))
print(f"o fatorial de {n1} é {fatorial(n1)}")