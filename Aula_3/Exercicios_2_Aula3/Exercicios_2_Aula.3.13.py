# Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)

n = int(input("Digite um número: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)