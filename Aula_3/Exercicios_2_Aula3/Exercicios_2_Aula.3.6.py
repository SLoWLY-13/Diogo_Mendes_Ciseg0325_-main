# Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos. 
contador = 0
numero = 2

while contador < 10:
    div = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            div += 1
    if div == 2:
        print(numero)
        contador += 1
    numero += 1