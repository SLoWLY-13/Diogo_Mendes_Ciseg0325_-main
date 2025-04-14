#

def validar_nome(nome):
    if len(nome) == 0:
        return False
    if not nome[0].isupper():
        return False
    for letra in nome[1:]:
        if not letra.islower() and letra not in "áéíóúâêôãõçà":
            return False
    return True

def adicionar(lista):
    primeiro = input("Primeiro nome: ")
    ultimo = input("Último nome: ")
    if not validar_nome(primeiro) or not validar_nome(ultimo):
        print("Nome inválido! Use letra inicial maiúscula e acentuação correta.")
        return
    idade = input("Idade: ")
    if not idade.isdigit():
        print("Idade inválida!")
        return
    lista.append([primeiro, ultimo, int(idade)])
    print("Pessoa adicionada com sucesso.")

def ordenar_ascii(lista, index):
    return sorted(lista, key=lambda x: [ord(c) for c in x[index]])

def listar(lista, tipo):
    if tipo == "primeiro":
        ordenada = ordenar_ascii(lista, 0)
    else:
        ordenada = ordenar_ascii(lista, 1)
    for p in ordenada:
        print(f"{p[0]} {p[1]} ({p[2]} anos)")

def remover(lista, tipo):
    nome = input(f"Digite o {tipo} nome para remover: ")
    index = 0 if tipo == "primeiro" else 1
    for p in lista:
        if p[index] == nome:
            lista.remove(p)
            print("Removido com sucesso.")
            return
    print("Nome não encontrado.")

def menu():
    lista = []
    while True:
        print("\n1. Adicionar")
        print("2. Listar por primeiro nome")
        print("3. Listar por último nome")
        print("4. Remover por primeiro nome")
        print("5. Remover por último nome")
        print("6. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar(lista)
        elif opcao == "2":
            listar(lista, "primeiro")
        elif opcao == "3":
            listar(lista, "último")
        elif opcao == "4":
            remover(lista, "primeiro")
        elif opcao == "5":
            remover(lista, "último")
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

menu()
