
class Carros:
    def __init__ (self,modelo,marca,ano,velocidade):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.velocidade = velocidade

    def Acelera(self, nivel):
        self.velocidade += nivel
        print(f"A velocidade atual é {self.velocidade} km/h")