# Exercício 7: O sistema de avaliação de determinada disciplina, é composto por três provas Nota (0 a 10). A primeira prova tem peso 2, a Segunda tem peso 3 e a terceira prova tem peso 5. Faça um algoritmo para calcular a média final de um aluno desta disciplina e se a média for maior ou igual a 6, mostrar APROVADO, senão, mostrar REPROVADO. 

nota1 = float(input("Nota da primeira prova (0 a 10): "))
nota2 = float(input("Nota da segunda prova (0 a 10): "))
nota3 = float(input("Nota da terceira prova (0 a 10): "))

peso1 = 2
peso2 = 3
peso3 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

if media >= 6:
    print(f"Média: {media: } - APROVADO")
else:
    print(f"Média: {media: } - REPROVADO")