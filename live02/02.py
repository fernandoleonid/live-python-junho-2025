nome_aluno = input ("Digite seu nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

# A --> 10
# B --> 8 |-- 10
# C --> 5 |-- 8 
# D --> 3 |-- 5
# E --> 0 -- 3  
# F --> 0

if media == 10:
    situacao = "A"
elif media >= 8:
    situacao = "B"
elif media >= 5:
    situacao = "C"
elif media >= 3:
    situacao = "D"
elif media > 0:
    situacao = "E"
else:
    situacao = "F"

if situacao == "D":
    nota_recuperacao = float(input("Digite a nota de recuperacao: "))
    media = (media + nota_recuperacao) / 2
    if media == 10:
        situacao = "A"
    elif media >= 8:
        situacao = "B"
    elif media >= 5:
        situacao = "C"
    elif media >= 3:
        situacao = "D"
    elif media > 0:
        situacao = "E"
    else:
        situacao = "F"

print (f"O aluno {nome_aluno} com a média {media} está {situacao}")