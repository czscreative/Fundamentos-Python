# Exercício 4.7 - Analise o programa 4.3. Faz sentido usar o else nesse programa? Explique a resposta.
salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: R$ {salario:6.2f} Imposto a pagar: R$ {imposto:6.2f}")

""" Não é possível o uso do ELSE nesse programa, dado que os IFs são executados sequencialmente, onde dependendo do valor, o primeiro pode ser executado ou não, mas se o valor for acima de R$ 3000, necessáriamente, todos os IFs serão executados."""
