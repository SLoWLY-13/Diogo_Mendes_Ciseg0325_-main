# Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.

n = int(input("Digite um número: "))
cont = 0

for i in range(1, n):
    print(n, "+", i, "=", n + i)
    cont += 1

    print(n, "-", i, "=", n - i)
    cont += 1

    print(n, "*", i, "=", n * i)
    cont += 1

    print(n, "/", i, "=", n / i)
    cont += 1

print("Total de operações:", cont)

