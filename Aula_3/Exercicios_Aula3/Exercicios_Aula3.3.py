#Exercício 3: Crie 2 variáveis (num1 e num2) e leia o valor para cada um deles. Mostre os valores de forma crescente e decrescente. 
num1 = int(input("primeiro número: "))
num2 = int(input("segundo número: "))

if num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")
