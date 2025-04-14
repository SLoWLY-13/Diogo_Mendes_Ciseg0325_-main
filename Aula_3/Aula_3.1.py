#match case compara a igualdade entre elementos

opt="0"
print("press RK - Rock")
print("press PP - Pop")
print("press JZ - Jazz")

opt=input("Introduz opçao")

match opt:
    case 1:
        print("Ouvir rock")
    case 2:
        print("Ouvir pop")
    case 3:
        print("Ouvir jazz")
    case _:
        print("sem opcao nao existe")