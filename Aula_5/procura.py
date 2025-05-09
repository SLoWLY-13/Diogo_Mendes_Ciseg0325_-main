# Algoritmo para procura
import time
nomeproc=""
contaigualdade=0
#index i      0             1               2               3
nomes=["Dario Quental","Joao Matos", "Liliana Queiroz","Joao Matos"]
#index it 0123456789101112,0123456789,01234567891011121314,0123456789
#Nomes[i][it]

nomeproc=input("Introduz nome de busca")

for i in range(len(nomes)):
    print(f"valor de i no for externo roda 1 dimensao da lista", i)
    contaigualdade=0
    print()
    for it in range(len(nomes[i])):
        time.sleep(1)
        print(f"valor e it no for interno", it)
        print(nomes[i][it])
        print (len(nomeproc[it]))
        if ord(nomes[i][it]) == ord(nomeproc[it]):
            contaigualdade +=1
        print("igualdade = ",contaigualdade)
        if contaigualdade==len(nomeproc):
            print ("nome em nomes",nomes[i], "posiçao da lista")
            print("nome em nomeproc", nomeproc)
        if it== (len(nomeproc)-1):
            print("tamanho do valor nomeproc",len(nomeproc))
            break