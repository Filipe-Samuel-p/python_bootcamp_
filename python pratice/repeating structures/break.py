

quantidade_de_numerosLidos = int(input("Digite a quantidade de numeros que serao lidos: "))
numeros_pares = 0 
for i in range(quantidade_de_numerosLidos):
    numeros_Digitados = int(input("Digite um numero (1000 acaba a leitura): "))
    if numeros_Digitados % 2 == 0:
       numeros_pares += 1
       if numeros_Digitados == 1000:
           break

print(f"o numero de valores lidos foi {quantidade_de_numerosLidos}")
print(f"a quantidade de numeros pares foi lidos foi {numeros_pares}")


# exercice 2

while True:
    numero = float(input("Digite um numero: "))
    if numero == 0 or numero < 0:
      print("Valor invalido")
      break
    else:
      print(f"o cubo do numero é {numero ** 3}")
      print(f"o quadrado do numero é {numero ** 2}")
      print(f"a raiz quadrada do numero é {numero ** 1/2}")