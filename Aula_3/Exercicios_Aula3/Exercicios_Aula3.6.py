# Exercício 6: Uma loja oferece para os seus clientes, um determinado desconto de acordo com o valor da compra efetuada. O desconto é de 10%, se o valor da compra for até 200.00€, 15% se for maior que 200€ e menor ou igual a  500,00E e 20% se for acima de 500,00€. Crie um algoritmo que leia o nome do cliente e o valor da compra. Mostre ao final o nome do cliente, o valor da compra, o percentual de desconto e o seu valor e valor total a pagar deste cliente. (só fazer duas Contas) 

nome = input("Nome do cliente: ")
valor = float(input("Valor da compra: "))

if valor <= 200:
    desconto = 10
elif valor <= 500:
    desconto = 15
else:
    desconto = 20

desc = valor * desconto / 100
total = valor - desc

print("Cliente:", nome)
print("Valor da compra:", valor)
print("Desconto:", desconto, "%")
print("Valor do desconto:", desc)
print("Total a pagar:", total)