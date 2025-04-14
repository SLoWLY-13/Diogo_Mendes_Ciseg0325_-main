# Exercício 5: Ler 3 valores INTEIROS para as variáveis Num1, Num2, Num3. Apresentar os valores dispostos em ordem crescente e decrescente

num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))
num3 = int(input("terceiro numero: "))

numeros = [num1, num2, num3]
numeros.sort()

print(f"Crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
print(f"Decrescente: {numeros[2]}, {numeros[1]}, {numeros[0]}")
