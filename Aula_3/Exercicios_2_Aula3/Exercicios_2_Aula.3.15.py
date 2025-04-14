# Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.

i = 0
while i <= 255:
    for j in range(20):
        if i > 255:
            break
        print(i, "->", chr(i))
        i += 1
    resp = input("Pressione Enter para continuar ou digite 'sair' para terminar: ")
    if resp.lower() == "sair":
        break