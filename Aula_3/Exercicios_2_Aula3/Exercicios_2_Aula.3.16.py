# Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.

soma = 0
cont = 0

while cont < 30:
    n = int(input("Digite um número par entre 1 e 50: "))
    if n >= 1 and n <= 50 and n % 2 == 0:
        soma += n
        cont += 1
    else:
        print("Número inválido. Tente novamente.")

media = soma / 30
print("A média dos 30 números pares é:", media)