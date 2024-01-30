import os
from logo import logo

dicionario ={}
parametro = 0
print(logo)
while True:
   nome_do_usuario = input("Qual o seu nome? ")
   valor_pago = float(input("De quanto será o lance: "))
   dicionario[nome_do_usuario] = valor_pago
   if valor_pago >= parametro:
      parametro = valor_pago
      nome_de_quem_tem_o_maior_valor = nome_do_usuario

   verificacao = input("Existem mais pessoas para jogar? (sim) ou (nao): ")
   
   if verificacao.lower() == "sim":
      os.system("clear")  #limpa o terminal  
      continue
   else:
      break
print(f"o maior valor é de { nome_de_quem_tem_o_maior_valor} e a quantia foi de {parametro}")

