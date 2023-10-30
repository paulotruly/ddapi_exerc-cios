import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
    return tarefas

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefa(tarefas, descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. [{status}] {tarefa['descricao']}")

def marcar_como_concluida(tarefas, numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        salvar_tarefas(tarefas)
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(tarefas, numero):
    if 1 <= numero <= len(tarefas):
        del tarefas[numero - 1]
        salvar_tarefas(tarefas)
    else:
        print("Número de tarefa inválido.")

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
            print("Tarefa adicionada com sucesso.")
        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("Tarefas:")
                listar_tarefas(tarefas)
        elif opcao == "3":
            listar_tarefas(tarefas)
            numero = int(input("Digite o número da tarefa concluída: "))
            marcar_como_concluida(tarefas, numero)
        elif opcao == "4":
            listar_tarefas(tarefas)
            numero = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, numero)
        elif opcao == "5":
            print("Obrigado por usar o aplicativo de gerenciamento de tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
