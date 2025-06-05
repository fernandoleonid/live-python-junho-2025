# Você foi contratado por uma empresa de tecnologia 
# para desenvolver um programa em Python 
# que calcule o ano de nascimento de uma 
# pessoa com base na idade informada.


ano_atual = 2025
nome = input ("Digite seu nome: ")
idade = int( input ("Digite sua idade: ") )

ano_nascimento = ano_atual - idade

print (f"{nome} vc nasceu em {ano_nascimento}")
