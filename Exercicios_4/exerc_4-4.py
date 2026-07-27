# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario_atual = float(input("Informe seu salário atual "))
if salario_atual > 1250:
    aumento = salario_atual * 0.1
    novo_salario = salario_atual + aumento
    print(
        f"O seu salário teve aumento de R$ {aumento:5.2f} e o valor final ficou em R$ {novo_salario:5.2f}."
    )

if salario_atual <= 1250:
    aumento = salario_atual * 0.15
    novo_salario = salario_atual + aumento
    print(
        f"O seu salário teve aumento de R$ {aumento:5.2f} e o valor final ficou em R$ {novo_salario:5.2f}."
    )
