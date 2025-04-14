# Exercício 2: Ler 10 números, e determinar se o número par e número impar. 
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        print("É par\n")
    else:
        print("É ímpar\n")