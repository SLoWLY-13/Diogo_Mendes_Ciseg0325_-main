# Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média. 
soma = 0

for i in range(10):
    nota = float(input(f"Nota do {i+1} aluno: "))
    soma += nota

media = soma / 10
print(f"\nA média das notas é: {media}")