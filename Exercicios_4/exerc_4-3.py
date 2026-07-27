# Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor valor.
valor_1 = int(input("Informe o primeiro valor "))
valor_2 = int(input("Informe o segundo valor "))
valor_3 = int(input("Informe o terceiro valor "))

if valor_1 < valor_2 & valor_2 < valor_3:
    print(f"Menor: {valor_1}, Maior: {valor_3}")

if valor_2 < valor_3 & valor_3 < valor_1:
    print(f"Menor: {valor_2}, Maior: {valor_1}")

if valor_3 < valor_1 & valor_1 < valor_2:
    print(f"Menor: {valor_3}, Maior: {valor_2}")
