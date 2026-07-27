# Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Informe o valor do salário: "))
aumento = float(input("Informe a porcentagem do aumento: "))

aumento_salario = salario * (aumento / 100)
novo_salario = salario + aumento_salario

print(
    f"O salário de R$ {salario:5.2f} tevem um reajuste de R$ {aumento_salario:5.2f} e agora está em R$ {novo_salario:5.2f}"
)
