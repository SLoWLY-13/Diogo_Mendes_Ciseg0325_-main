numeros=[1,4,5,6,7]

def listar(nummeros):
    try:
        for i in range(len(nummeros)+2):
            print(nummeros[i])
    except Exception as error:
        print ("erro no programa  ",type(error).__name__ , "    ", error)


def adicionar(nummeros,inputdinamico):
    nummeros.append(inputdinamico)
    return nummeros

listar(numeros)
num=int(input("Digite um número: "))
numeros=adicionar(numeros,num)
nome=input("Digite um nome: ")
numeros=adicionar(numeros,nome)
listar(numeros)