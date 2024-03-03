# sorteio de um numero


numero_sorteado = int(input("sorteie um valor entre 1 e 10: ")) #poderia ser colocado um numero maior que 10
tenativas = 0
if numero_sorteado < 0 or numero_sorteado > 10 or numero_sorteado == 0:
  print("voce nao digitou um numero entre 1 e 10,por favor,tente de novo")
else:
  while True:
      numero2 = int(input("tente acertar o valor sorteado: "))
      tenativas += 1
      if numero2 < 0 or numero2 == 0 or numero2 > 10:
         print("Digite um numero entre 1 e 10")
      elif numero2 < numero_sorteado:
        print("o numero digitado e menor que o valor sorteado")
        continue
      elif numero2 > numero_sorteado:
        print("o numero digitado e maior que o valor sorteado")
        continue
      else: 
        print("PARABENS!!! ACERTOU O NUMERO: ")
        print(f"o numero sorteado foi {numero_sorteado} ")
        print(f"o numero de tentativas foi {tenativas} ")
        break

