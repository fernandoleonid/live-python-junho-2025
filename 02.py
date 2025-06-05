# Você é um programador que trabalha em uma loja virtual 
# que vende produtos eletrônicos. A sua tarefa é criar 
# um programa em Python que calcule o preço final 
# de um produto após o acréscimo de impostos e descontos, 
# e exibir na tela o valor final que será cobrado do cliente.


preco = float(input("Digite o preço do produto: "))
imposto = float(input("Digite o valor do imposto: "))
desconto = float(input("Digite o valor do desconto: "))
 
preco_final = preco + imposto - desconto

print (f"O preço final é {preco_final}")