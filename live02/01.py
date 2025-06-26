nome_aluno = input ("Digite seu nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if media >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print (f"O aluno {nome_aluno} com a média {media} está {situacao}")