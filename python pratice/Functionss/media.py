def media_ari(x,y,z):
    media = (x+y+z)/3
    return media

def media_pond(x,y,z):
    media = (x*5 + y* 3 + z* 2)/ 10
    return media 


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print("\n")
while True:
    print("Escolha 'A' para a media aritimetica")
    print("Escolha 'P' para a media ponderada")
    opcao = input("Qual foi a opcao escolhida?: ")
    if opcao.lower() == "a":
        print (f"A média aritimética é : {media_ari(n1,n2,n3)}")
        break
    elif opcao.lower() == "p":
        print (f"A média ponderada é : {media_pond(n1,n2,n3)}")
        break 
    else:
        print("Digite uma opcao válida\n")
        continue 