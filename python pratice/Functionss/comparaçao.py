
# Dados dois numeros, verifica qual é o maior 

def maior_valor(a,b):
    if a > b:
        return print(f"o numero {a} é maior que o numero {b}")
    elif a == b:
        return print("os valores sao iguais")
    else:
        return print(f"o valor {b} é maior que o valor {a}")
    
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um segundo valor: "))
maior_valor(n1,n2)