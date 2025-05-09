#Exercício Sort 1 
#Listas de Caracteres (ASCII) 
#Escreva um programa que aceite a entrada de primeiro e último nome e valide se os mesmos nomes estão corretos, 
# (Exemplo de nome correto: Timóteo Amaro, primeira Letra de cada nome GRANDE 
# O resto pequeno considerar o uso de entoação portuguesa (´ ` ~ ^) uso de tabela ASCII)
#  O programa deve parar de inserir nomes quando o utilizador assim o desejar. 
# Ainda deve ter a opção de listar por ordem de primeiro nome e último nome. Exemplo de lista por Primeiro nome: 
#João Messias
#Mário Silva
#Paulo Lima
#Último nome:
#Paulo Lima
#João Messias
#Mário Silva
#(Usar a tabela ASCII para ordenar obrigatório.)
#O programa deve também manter a idade de cada pessoa introduzida e permitir apagar nomes por primeiro ou último validando e informando se existe o nome na lista e apagando a idade e nome correspondente.
#Funções permitidas (adicionar na lista, remover da lista, ord , chr)


def validar_nome(nome):
    if len(nome) == 0:
        return False
    primeira_letra = nome[0]
    restante = nome[1:]
    return primeira_letra.isupper() and restante.islower()

def adicionar_pessoa(lista):
    primeiro = input("Primeiro nome: ").strip()
    if not validar_nome(primeiro):
        print("Primeiro nome inválido!")
        return
    ultimo = input("Último nome: ").strip()
    if not validar_nome(ultimo):
        print("Último nome inválido!")
        return
    idade = input("Idade: ").strip()
    if not idade.isdigit():
        print("Idade inválida!")
        return
    lista.append((primeiro, ultimo, int(idade)))
    print("Pessoa adicionada com sucesso.")

def ordenar_por_ascii(lista, por='primeiro'):
    index = 0 if por == 'primeiro' else 1
    return sorted(lista, key=lambda x: [ord(c) for c in x[index]])

def listar_pessoas(lista):
    if not lista:
        print("Lista vazia.")
        return
    escolha = input("Ordenar por (primeiro/ultimo): ").strip().lower()
    if escolha not in ['primeiro', 'ultimo']:
        print("Escolha inválida.")
        return
    ordenada = ordenar_por_ascii(lista, por=escolha)
    print("Lista de pessoas:")
    for p in ordenada:
        print(f"{p[0]} {p[1]} - {p[2]} anos")

def remover_pessoa(lista):
    escolha = input("Remover por (primeiro/ultimo): ").strip().lower()
    if escolha not in ['primeiro', 'ultimo']:
        print("Escolha inválida.")
        return
    nome = input("Nome a remover: ").strip()
    index = 0 if escolha == 'primeiro' else 1
    for i, pessoa in enumerate(lista):
        if pessoa[index] == nome:
            print(f"{pessoa[0]} {pessoa[1]} removido com sucesso.")
            lista.pop(i)
            return
    print("Nome não encontrado.")

def menu():
    lista_pessoas = []
    while True:
        print("\nMenu:")
        print("1 - Adicionar pessoa")
        print("2 - Listar pessoas")
        print("3 - Remover pessoa")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionar_pessoa(lista_pessoas)
        elif opcao == '2':
            listar_pessoas(lista_pessoas)
        elif opcao == '3':
            remover_pessoa(lista_pessoas)
        elif opcao == '4':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida.")

menu()
