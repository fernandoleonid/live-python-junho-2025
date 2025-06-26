contador = 1
while contador <= 5:
    nome = input ("Digite seu nome: ")
    media = float (input("Digite sua média: "))
    if media >= 5:
        print ("Aprovado")
    else:
        print ("Reprovado")
    contador += 1