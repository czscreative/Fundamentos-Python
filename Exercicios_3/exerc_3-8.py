# Exercício 3.8 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
valor_metros = float(input("Informe o valor em metros:"))

milimetros = valor_metros * 1000

print(f"O valor de {valor_metros:1.0f}m em milímetros é {milimetros:5.0f}mm")