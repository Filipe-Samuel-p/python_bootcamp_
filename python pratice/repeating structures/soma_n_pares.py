# calcule e mostre a soma dos 50 primeiros pares:

soma = 0
for i in range(1,51):
    if i % 2 == 0:
      print(i)
      soma += i
print(f"a soma dos numeros é {soma}")
