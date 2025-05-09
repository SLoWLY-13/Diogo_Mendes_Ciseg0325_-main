def eh_primo(n): return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
def divisores(n): return [i for i in range(1, n+1) if n % i == 0]
def eh_perfeito(n): return sum(divisores(n)) - n == n

def ver_numeros():
    lista = []
    while len(lista) < 50:
        try:
            n = int(input("Número (1-1000): "))
            if not 1 <= n <= 1000: continue
            lista.append(n)
            print("Par" if n % 2 == 0 else "Ímpar")
            print("Primo" if eh_primo(n) else "Não primo")
            divs = divisores(n)
            print(f"Divisores ({len(divs)}):", divs)
            print("Perfeito" if eh_perfeito(n) else "Não perfeito\n")
            if len(lista) % 10 == 0 and input("Continuar? (s/n): ") != 's': break
        except: print("Erro")

def calculadora():
    ops = {'1': '+', '2': '-', '3': '*', '4': '/'}
    cont = 0
    while True:
        print("1-Soma 2-Sub 3-Mult 4-Div")
        o = input("Escolha operação: ")
        if o not in ops: continue
        try:
            a = int(input("A (1-1000): "))
            b = int(input("B (1-1000): "))
            if not (1 <= a <= 1000 and 1 <= b <= 1000): continue
            if o == '1': print(a + b)
            elif o == '2': print(a - b)
            elif o == '3': print(a * b)
            elif o == '4': print(a / b if b != 0 else "Erro: div/0")
            cont += 1
            if cont % 5 == 0 and input("Continuar? (s/n): ") != 's': break
        except: print("Erro")

def menu_numeros_calculadora():
    while True:
        m = input("\n1-Ver números 2-Calculadora 3-Voltar: ")
        if m == '1': ver_numeros()
        elif m == '2': calculadora()
        elif m == '3': break

marcas, modelos = [], []

def menu_carros():
    while True:
        m = input("\n1-Cadastrar 2-Procurar 3-Eliminar 4-Voltar: ")
        if m == '1':
            if len(marcas) < 100:
                marcas.append(input("Marca: "))
                modelos.append(input("Modelo: "))
            else: print("Limite atingido.")
        elif m == '2':
            termo = input("Buscar: ").lower()
            for i, (ma, mo) in enumerate(zip(marcas, modelos)):
                if termo in ma.lower() or termo in mo.lower():
                    print(f"[{i}] {ma} - {mo}")
        elif m == '3':
            try:
                i = int(input("Posição a eliminar: "))
                print("Removido:", marcas.pop(i), modelos.pop(i))
            except: print("Erro")
        elif m == '4': break

while True:
    op = input("\n1-Números/Calculadora 2-Carros 3-Sair: ")
    if op == '1': menu_numeros_calculadora()
    elif op == '2': menu_carros()
    elif op == '3': print("Saindo..."); break


