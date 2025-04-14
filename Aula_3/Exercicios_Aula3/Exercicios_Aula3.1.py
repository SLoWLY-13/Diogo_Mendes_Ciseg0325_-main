# Exercício 1: Desenvolva um programa que assuma uma entrada em Segundos e transforme em Horas, Minutos e Segundos. 

segundos = int(input("Digite os segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas}h {minutos}m {segundos}s")



