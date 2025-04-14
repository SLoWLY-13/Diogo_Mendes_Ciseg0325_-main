# Exercício 2: Fazer um programa que analise 3 valores inteiros (através das variáveis num1, num2 e num3), e informa qual o maior e qual o menor deles.  

num1=0
num2=0
num3=0

num1=int(input("Primeiro numero: "))
num2=int(input("Segundo numero:"))
num3=int(input("Terceiro numero:"))


if num1 > num2 and num2 > num3:
    print("num 1 é o maior, num 3 é o menor")
elif num1 > num3 and num3 > num2:
    print("num 1 é o maior, num 2 é o menor")
elif num2 > num1 and num1 > num3:
    print("num 2 é o maior , num 3 é o menor")
elif num2 > num3 and num3 > num1:
    print("num 3 é o maior, num 1 é o menor ")
elif num3 > num2 and num2 > num1:
    print("num 3 é o maior, num 1 é o menor")
elif num3 > num1 and num1 > num2:
    print("num 3 é o maior, num 2 é o menor")