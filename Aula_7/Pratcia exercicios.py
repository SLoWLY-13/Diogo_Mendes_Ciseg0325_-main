

def contagem_regressiva():
    numero = int(input("Escolha um número: "))
    while True:
        print(numero)
        numero -= 1
        if numero <= 0:
            break 
#contagem_regressiva()



def maior_numero(lista_numeros):
    maior_numero = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [2, 4, 8, 10, 23, 56, 12, 5]
maior_numero_lista = maior_numero(lista)
print(f"O maior numero da lista é {maior_numero_lista}")



def maior_numero(lista_numeros):
    maior_numero = max(lista_numeros)
    return maior_numero

lista = [2, 4, 8, 10, 23, 56, 12, 5]
maior_numero_lista = maior_numero(lista)
print(f"O maior numero da lista é {maior_numero_lista}")
