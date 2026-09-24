"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

deposito_inicial = float(input("Digite o aporte inicial: "))
aporte_recorrente = 0
taxa_juros = float(input("Digite a taxa de juros: "))
saldo = deposito_inicial
periodo = 12
mes = 1

while mes <= periodo:
    rendimento_mes = saldo * (taxa_juros / 100)
    saldo = saldo + rendimento_mes + aporte_recorrente
    print(f"O valor de lucro no mês {mes} foi de R$ {saldo:5.2f}")
    aporte_recorrente = float(input("Informe o aporte desse mês: "))
    mes += 1

print(
    f"O total ganho no período de {periodo} mês(es) foi de R$ {saldo:5.2f} com juros a {taxa_juros}%"
)
