import os

opcao = ""
banco_dados = []

def listar_tarefas ():
    contador = 0
    limpar_tela()
    print ("-----")
    for tarefa in banco_dados:
        print (f"{contador} - {tarefa}")
        print ("-----")
        contador += 1

def limpar_tela():
    os.system('cls')

def selecionar (opcao):
    if (opcao == "1"):
        tarefa = input ("Digite sua tarefa: ")
        banco_dados.append(tarefa)
    elif (opcao == "2"):
        listar_tarefas()
    elif (opcao == "3"):
        listar_tarefas()
        tarefa = int(input ("Escolha a tarefa para excluir: "))
        del banco_dados[tarefa]
    elif (opcao == "4"):
        listar_tarefas()
        tarefa = int(input ("Escolha a tarefa para editar: "))
        nova_tarefa = input ("Digite a nova tarefa: ")
        banco_dados[tarefa] = nova_tarefa
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