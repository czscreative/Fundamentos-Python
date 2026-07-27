# Exercício 4.1 - Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valor forem iguais? Explique.
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print("O primeiro valor é maior!")
if b > a:
    print("O segundo valor é maior!")

# Se os valores forem iguais, nenhum dos blocos IF serão executados.
