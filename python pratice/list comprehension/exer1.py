#list comprehension é uma forma de escrever uma nova lista de maneira bem simples
# em uma linha de código.
# sintaxe sintaxe: nova_lista = [ novo_item for item in alguma_lista]
# Não é só usada com lista, pode ser usada com strings,range,por exemplo
#Lista comprehension com condicional: nova_lista = [novo_item for item in alguma_lista if teste(condicao)]

# Exemplo: Crie uma lista que adicione mais 2 em cada elemento da lista

lista1 = [1,2,3]
nova_lista=[]
for num in lista1:
    novo_elemento = num + 1
    nova_lista.append(novo_elemento)
print(nova_lista)

#list comprehension

""" new_list = [intem + 1 for intem in lista1]
print(new_list) """

""" nome = "filipe"
lista_nome = [letra for letra in nome]
print(lista_nome) """ 

""" dobro = [n * 2 for n in range(1,5)]
print(dobro) """

numeros_pares = [n for n in range(1,11) if n%2 == 0]
print(numeros_pares)