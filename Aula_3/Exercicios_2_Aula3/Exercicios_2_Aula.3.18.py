#Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
#6=3+2+1  

n = int(input("Número: "))
contador = 0

def numero_perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma == num

for i in range(1, n+1):
    if numero_perfeito(i):
        contador += 1
        print(i, "é um número perfeito.")

print(f"Existem {contador} números perfeitos até {n}.")