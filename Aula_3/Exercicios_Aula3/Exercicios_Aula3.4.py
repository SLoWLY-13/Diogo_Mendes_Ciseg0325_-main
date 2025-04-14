#Exercício 4: Fazer um algoritmo que leia o saldo inicial de cliente do banco e leia também um cheque que entrou e ANALISE se o cheque poderá ser descontado ou não, já que este cliente não possui limite. Se o cheque não poderá ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo.  

saldo = float(input("Saldo inicial: "))
cheque = float(input("Valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado! Saldo atual: {saldo: }")
else:
    print("Saldo insuficiente.")