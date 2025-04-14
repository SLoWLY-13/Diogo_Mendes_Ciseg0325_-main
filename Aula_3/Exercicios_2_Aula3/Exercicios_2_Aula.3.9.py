# Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. 
numero = 0

while numero < 1 or numero > 100:
    numero = int(input("Digite um número entre 1 e 100: "))

print("Número válido:", numero)
