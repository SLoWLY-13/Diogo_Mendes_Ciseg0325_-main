# Exercício “match case”: Ler para uma variável INTEIRA um número de 1 a 12 e mostrar o nome do mês correspondente. Caso o mês não existir, mostrar essa informação. 
mes = int(input("Número de 1 a 12: "))

match mes:
    case 1: print("Janeiro")
    case 2: print("Fevereiro")
    case 3: print("Março")
    case 4: print("Abril")
    case 5: print("Maio")
    case 6: print("Junho")
    case 7: print("Julho")
    case 8: print("Agosto")
    case 9: print("Setembro")
    case 10: print("Outubro")
    case 11: print("Novembro")
    case 12: print("Dezembro")
    case _: print("Mês inválido!")