# Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui. 

numero = int(input("Digite um número: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

print(divisores)
