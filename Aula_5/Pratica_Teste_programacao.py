

def eh_primo(n):                                                            # Verifica se um número é primo
    if n <= 2:
        return False                                                        # Rejeita numeros menores que 2
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True                                                             # Se não for divisível por nenhum número, é primo

def eh_perfeito(n):
    soma = sum(i for i in range(1, n) if n % i == 0)
    return soma == n                                                        # Verifica se o numero é perfeito   

def analise_numero(n):
    primo = eh_primo(n)                                                     
    perfeito = eh_perfeito(n)
    divisores = [i for i in range(1, n+1) if n % i == 0]
    par_ou_impar = "Par" if n % 2 == 0 else "Ímpar"
    print(f"\nNúmero: {n}")
    print(f" - Primo: {'Sim' if primo else 'Não'}")                         # Recebe um numero n e diz se é: perfeito,primo,par ou impar e quantos divisores tem
    print(f" - Perfeito: {'Sim' if perfeito else 'Não'}")
    print(f" - Quantidade de divisores: {len(divisores)}")
    print(f" - Par ou Ímpar: {par_ou_impar}")

def menu_numeros():
    numeros = []
    while len(numeros) < 50:                                                # Cria uma lista para armazenar os numeros analisados e permite no maximo 50 entradas
        for _ in range(10):
            if len(numeros) >= 50:
                break                                                       # Pede até 10 numeros por vez e depois pergunta se o utilizador quer continuar
            try:
                n = int(input("Insira um número entre 1 e 1000: "))
                if 1 <= n <= 1000:
                    numeros.append(n)
                    analise_numero(n)
                else:
                    print("Número inválido.")
            except ValueError:                                              # try/except evita erros se o input não for numero
                print("Entrada inválida.")                                  # Pede um numero e verifica se esta entre 1 e 1000,se for valido analisa e guarda
        op = input("\nDeseja continuar? (s/n): ").lower()
        if op != 's':
            break                                                           # A cada 10 valores pergunta se é para continuar

def calculadora():
    cont = 0
    while True:                                                             # Calculadora em loop infinito , conta quantas operações forem feitas
        try:
            a = int(input("Número 1 (1-1000): "))
            b = int(input("Número 2 (1-1000): "))                           # Pede 2 numeros validos de 1 a 1000
            if not (1 <= a <= 1000 and 1 <= b <= 1000):
                print("Números fora do intervalo.")
                continue                                                    # Se os valoresestiverem fora do intervalo ,reinicia o ciclo
            print("Operações: 1-Soma 2-Subtração 3-Multiplicação 4-Divisão")
            op = input("Escolha a operação: ")                              # Pede ao utilizador que escolha a operação matematica
            if op == '1':
                print("Resultado:", a + b)
            elif op == '2':
                print("Resultado:", a - b)
            elif op == '3':
                print("Resultado:", a * b)
            elif op == '4':
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Divisão por zero!")
            else:                                                           # No caso da divisão evita dividir por 0
                print("Operação inválida.")                                 # Executa a operação matematica escolhida
            cont += 1
            if cont % 5 == 0:
                voltar = input("Deseja continuar na calculadora? (s/n): ").lower()
                if voltar != 's':
                    break
        except ValueError:                                                  # A cada 5 operações pergunta se o utilizador quer continuar
            print("Entrada inválida.")                                      # try/except lida com entradas invalidas                              

def menu_carros():
    marcas = []
    modelos = []                                                            # Cria 2 listas 1 para marcas outra para modelos
    while True:
        print("\n===== Menu Carros =====")
        print("1 - Cadastrar marca e modelo")
        print("2 - Procurar marca ou modelo")
        print("3 - Excluir por posição")
        print("4 - Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")                              # Mostra o menu e lê a opção do utilizador

        if escolha == '1':
            if len(marcas) < 100:
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                marcas.append(marca)
                modelos.append(modelo)
                print("Carro adicionado com sucesso.")
            else:
                print("Limite de 100 carros atingido.")                       # Permite listar carros (marca + modelo) ate 100 no total
        elif escolha == '2':
            termo = input("Digite marca ou modelo para buscar: ").lower()
            for i in range(len(marcas)):
                if termo in marcas[i].lower() or termo in modelos[i].lower():
                    print(f"Posição {i} - Marca: {marcas[i]}, Modelo: {modelos[i]}")   # Pesquisa marcas ou modelos que contenham o texto digitado (sem diferenciar maiúsculas/minúsculas).
        elif escolha == '3':
            try:
                pos = int(input("Digite a posição para excluir: "))
                if 0 <= pos < len(marcas):
                    print(f"Removido: {marcas[pos]} {modelos[pos]}")
                    marcas.pop(pos)
                    modelos.pop(pos)
                else:
                    print("Posição inválida.")
            except ValueError:                                                  # Permite excluir um carro com base na posição da lista.
                print("Entrada inválida.")
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")                                            # Volta ao menu principal ou mostra erro se a opção não for reconhecida.                                   

def main():
    while True:
        print("\n======= MENU PRINCIPAL =======")
        print("1 - Ver números")
        print("2 - Calculadora")
        print("3 - Gerenciar Carros")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")                                     # Mostra o menu principal e pergunta o que o utilizador quer fazer.
        if opcao == '1':
            menu_numeros()
        elif opcao == '2':
            calculadora()
        elif opcao == '3':
            menu_carros()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
                                                                                  # Executa o programa
main()                                                                            # Este é o ponto de partida do programa, que chama o main().

