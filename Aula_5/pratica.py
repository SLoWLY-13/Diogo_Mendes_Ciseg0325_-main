
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


def main():
    while True:
        print("\n======= MENU PRINCIPAL =======")
        print("1 - Ver números")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")                                     # Mostra o menu principal e pergunta o que o utilizador quer fazer.
        if opcao == '1':
            menu_numeros()
        elif opcao == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
                                                                                  # Executa o programa
main()                         