# Função Input
# Tipos de dados primarios
# int 0... 9 ex: 1234567890
# float 1,0 ... 9.0 ex:1.1 / 1.2 / 1.3 / 1.4 / 1.5
# str "abcdefghijklmnopqrstuvxyz"
# bool "True/False"
# casting "cast" converte um tipo de dados em outro
# input serve para ir buscar uma variavel que o utilizador dá

num1=0
num2=0
total=0

num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))

print("Tipo do Numero1:",type(num1),"\nTipo do Numero:"+str(type(num2)))
total=num1+num2
print ("A soma do dois é:",total)
