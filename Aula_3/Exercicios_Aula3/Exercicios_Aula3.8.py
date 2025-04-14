# Exercício 8: Crie um programa que leia a nota de 10 alunos, calcule a média e mostre essa média e mostre também quantos alunos ficaram com a sua nota igual ou acima da média. (NOTAS de 0 a 20).  

notas = []
alunos_acima_da_media = 0

for i in range(10):
    nota = float(input(f"Nota do aluno {i + 1} (0 a 20): "))
    notas.append(nota)

media = sum(notas) / 10

for nota in notas:
    if nota >= media:
        alunos_acima_da_media += 1

print(f"Média das notas: {media: }")
print(f"Quantidade de alunos com nota igual ou acima da média: {alunos_acima_da_media}")