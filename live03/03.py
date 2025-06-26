import os

opcao = ""
banco_dados = []

def limpar_tela():
    os.system('cls')

def selecionar (opcao):
    if (opcao == "1"):
        tarefa = input ("Digite sua tarefa: ")
        banco_dados.append(tarefa)
    elif (opcao == "2"):
        limpar_tela()
        print ("-----")
        for tarefa in banco_dados:
            print (tarefa)
            print ("-----")
    elif (opcao == "3"):
        print ("Excluindo tarefa...")


    elif (opcao == "4"):
        print ("Editando tarefa...")
    elif (opcao == "0"):
        print ("Saindo do sistema...")
    else:
        print ("Opção invalida! Tente novamente")

def pausar_sistema ():
    input ("Digite ENTER para continuar...")

def mostrar_menu ():
    print ("1 - Adicionar tarefa")
    print ("2 - Listar tarefas")
    print ("3 - Excluir tarefa")
    print ("4 - Editar tarefa")
    print ("0 - Sair")

while (opcao != "0"):

    mostrar_menu()

    opcao = input("Escolha uma opção: ")
 
    selecionar(opcao)
    
    pausar_sistema()