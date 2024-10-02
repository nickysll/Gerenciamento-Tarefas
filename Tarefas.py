''Função principal:
Criar uma lista vazia para armazenar as tarefas

Enquanto o usuário não escolher sair:
    Mostrar menu de opções (Adicionar, Remover, Listar, Marcar como Concluída, Sair)
    Obter a escolha do usuário

    Se a escolha for "Adicionar":
        Obter a descrição da nova tarefa
        Criar uma nova tarefa com a descrição fornecida
        Adicionar a nova tarefa à lista de tarefas
        Mostrar mensagem de sucesso

    Se a escolha for "Remover":
        Listar todas as tarefas com índices
        Obter o índice da tarefa a ser removida
        Remover a tarefa com o índice fornecido da lista
        Mostrar mensagem de sucesso

    Se a escolha for "Listar":
        Listar todas as tarefas com seus estados (concluídas ou pendentes)

    Se a escolha for "Marcar como Concluída":
        Listar todas as tarefas pendentes com índices
        Obter o índice da tarefa a ser marcada como concluída
        Marcar a tarefa com o índice fornecido como concluída
        Mostrar mensagem de sucesso

    Se a escolha for "Sair":
        Encerrar o loop

Mostrar mensagem de despedida'''
#
# print("Lista de tarefas")
def mostra_menu():
    print("Selecione qual ação que deseja realizar:\n1-Adicionar Tarefa \n2-Remover Tarefa \n3-Listar minhas tarefas \n4- Marcar como concluida \n5- Sair")
    global opcao
    opcao = int(input("Escolha a opção: "))
    
lista_de_tarefas = []
​
def escolhe_status():
    print("1 - Não iniciada\n2 - Em andamento\n3 - Concluída")
    opcao = int(input("Escolha um status: "))
    if opcao == 1:
        return "Não iniciada"
    elif opcao == 2:
        return "Em andamento"
    elif opcao == 3:
        return "Concluída"
    else:
        print("Opção inválida!")
        return escolhe_status()
​
def adicionar_tarefa():
    nome = input("Digite o nome da sua tarefa: ")
    descricao = input("Digite a descrição da sua tarefa: ")
    status = escolhe_status()
    tarefa_nova = {"Nome da Tarefa": nome, "Descrição da Tarefa": descricao, "Status": status}

# Exibindo as tarefas existentes
    contador = 1
    for tarefa in lista_de_tarefas:
        print(f"Nome da Tarefa {contador}" + ": " + tarefa["Nome da Tarefa"])
        print(f"Descrição da tarefa {contador}" + ": " + tarefa["Descrição da Tarefa"])
        print(f"Status da tarefa {contador}" + ": " + tarefa["Status"])
        contador += 1

# Adicionando a nova tarefa e exibindo a mensagem de sucesso
    lista_de_tarefas.append(tarefa_nova)
    print(f"Tarefa {contador} adicionada com sucesso!")
    
def remover_tarefa():
    lista_de_tarefas
    try:
        numero_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= numero_tarefa <= len(lista_de_tarefas):
            tarefa_removida = lista_de_tarefas.pop(numero_tarefa - 1)
            print(f"Tarefa removida: {tarefa_removida['Nome da Tarefa']}")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")
    print("Tarefa excluida com sucesso!")
    
def tarefa_concluida():
    try:
        numero_tarefa = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
        
        if 1 <= numero_tarefa <= len(lista_de_tarefas):
            tarefa_numero = numero_tarefa - 1
            lista_de_tarefas[tarefa_numero]['status'] = "Concluída"
            tarefa_atualizada = lista_de_tarefas[tarefa_numero]
            print(f"Tarefa Concluída: {tarefa_atualizada['Nome da Tarefa']}")
            print("Tarefa atualizada com sucesso!")
        else:
            print("Número de tarefa inválido.")
    
    except ValueError:
        print("Por favor, digite um número válido.")
mostra_menu()
while opcao != 5:
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        remover_tarefa()
    elif opcao == 3:
        print(lista_de_tarefas)
    elif opcao == 4:
        tarefa_concluida()
​
    mostra_menu()
if opcao == 5:
    print("Saindo do programa. Até mais!")
