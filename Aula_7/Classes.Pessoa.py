
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def renovaridade(self, idade):
        self.idade = idade
        print("A sua idade foi alterada para",self.idade)
        return self.idade

Pessoas = []

for i in range(3):
    nom=input("Introduz um nome: ")
    idade=input("Introduza a sua idade: ")

    Pessoas.append(Pessoa(nom,idade))

    print("O seu nome é ",Pessoas[0].nom)
    print("E tem",Pessoas[0].idade, "anos")

    novaidade = input("Introduz nova idade:")

    Pessoas[i].renovaridade(novaidade)
    print("Nome", Pessoas[i].nom)
    print("Idade", Pessoas[i].idade)