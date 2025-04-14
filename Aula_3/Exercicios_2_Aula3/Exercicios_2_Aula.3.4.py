# Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não. 
n = int(input("Digite um número: "))
div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div += 1

if div == 2:
    print("É primo.")
else:
    print("Não é primo.")