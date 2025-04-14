# Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
# 1, 2, 3, 5, 8, 13, 21.
# Como se constrói.
# 1+1=2
#    1+2=3
#       2+3=5

a, b = 1, 1

for i in range(60):
    print(a, end=", " if i < 59 else "\n")
    a, b = b, a + b