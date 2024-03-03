# ARGUMENTOS NAO NOMEAVEIS: EMPACOTAMENTO E DESEMPACOTAMENTO 

def multiplicacao(*args):
    print(args)
    multi = 1
    for valor in args:
        multi *= valor
    return multi 

def criacao_da_lista():

 lista = []
 while True:
    valores = int(input("Digite um numero: "))
    lista.append(valores)
    opcao = input("Deseja sair? S OU N ")
    if opcao.lower() == 's':
        return lista
    else:
        continue

                                                                     # higher order functions
print(f"O valor da multiplicacao entre os numeros digitados foi {multiplicacao(*criacao_da_lista())}") 

 # como a funcao "criacao" retorna uma lista, usa o * para desempacotar a lista e usar os elementos como parametros da funcao "multiplicacao"
# como a funcao "multiplicacao" ira receber muitos parametros, cria-se uma variavel chamada "args" que sera uma tupla
# os elementos dessa tupla serao os argumentos nao nomeaveis passsados para a funcao multiplicacao
