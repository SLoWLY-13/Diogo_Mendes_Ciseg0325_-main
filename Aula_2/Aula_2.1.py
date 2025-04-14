#Operadores logicos
#compara 2 numeros ou strings e devolve sempre um valor Booleano (True ou FaLse)
# > maior , < menor , <= menor ou igual , >= maior ou igual , != diferente

#print(2<3) ->True
#print(2>3) ->False
#print(2=3) ->False

# AND para ser True ambas as condições tem de ser True
# OR sempre True ate ambas as condições serem False

#If,elif,else,match case

#entre o num1 e o num2 quem é o maior e o menor

num1=0
num2=0
num3=0

num1=int(input("Introduz um numero 1 : "))
num2=int(input("Introduz um numero 2 : "))

#if num1 > num2: 
#    print("num1 é maior e o num2 é o menor")
#else:
#
#      print("num2 é maior e o num1 é o menor")


#entre o num1 , num2 e num3 quem é o maior e o menor
#num1 > num2 && num1 > num3  num1 é o maior
#num2 > num1 && num2 > num3  num2 é o maior
#num3 > num2 && num3 > num1  num3 é o maior

if num1 > num2:
    if num1>num3:
        print("num 1 é o maior")
elif num2 > num1:
    if num2 > num3:
        print("num 2 é o maior")
elif num3 > num1:
    if num3 > num2:
        print("num 3 é o maior")
else:
    if num1 < num2:
        if num1 < num3:
            print("num 1 é o menor")
    elif num2 < num1:
        if num2 < num3:
            print("num 2 é o menor")
    elif num3 < num1:
        if num3 < num2:
            print("num 3 é o menor")


