import random

names = ["Filipe", "Samara", "Rildo", "Tania","Bia"]
dicionario = {chave:random.randint(1,100) for chave in names}
for valor in dicionario:
    print(valor,":",dicionario[valor])