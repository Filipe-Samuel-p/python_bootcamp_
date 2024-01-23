# Ideia: Gerar uma senha 

import random
 
def gerando_as_letras(x):
  global senha
  for i in range(x):
    senha.append(lista_letras[random.randint(0,51)])  # escolhe uma letra aleatoria da lista de acordo com o indice


def gerando_os_numeros(y):
  global senha
  for j in range(y):
    senha.append(lista_numeros[random.randint(0,9)])  #OBS: Aqui, o ultimo valor do randint pode ser incluido. 
                                                      # Cuidado para nao dar um erro de indexError
  
def gerando_os_simbolos(z):
  global senha
  for k in range(z):
    senha.append(lista_simbolos[random.randint(0,8)])


# MAIN

senha = [] 

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_simbolos  = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
total_de_letras= int(input("Quantas letras quer que sua senha tenha?\n")) 
total_de_simbolos = int(input("Quantos simbolos quer que sua senha tenha \n"))
total_de_numeros = int(input("Quantos numeros quer que sua senha tenha?\n"))
 
gerando_as_letras(total_de_letras)
gerando_os_simbolos(total_de_simbolos)
gerando_os_numeros(total_de_numeros)

random.shuffle(senha)  #embaralha a minha lista
senha_final = "".join(senha) #transforma minha lista em uma string

print(f"Sua senha é: {senha_final}")