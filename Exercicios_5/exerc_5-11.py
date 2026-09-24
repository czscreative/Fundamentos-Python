"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""

# Cálculo com juros simples
# deposito_inicial = float(input("Digite o depósito inical: "))
# taxa_juros = float(input("Digite a taxa de juros: "))
# saldo = deposito_inicial
# rendimento_mensal = deposito_inicial * (taxa_juros / 100)
# periodo = 24
# mes = 1

# while mes <= periodo:
#     saldo = saldo + rendimento_mensal
#     print(f"O valor de lucro no mês {mes} foi de R$ {saldo:5.2f}")
#     mes += 1

# print(
#     f"O total ganho no período de {periodo} mês(es) foi de R$ {saldo:5.2f} com juros a {taxa_juros}%"
# )

# Cálculo de Juros Compostos
deposito_inicial = float(input("Digite o depósito inical: "))
taxa_juros = float(input("Digite a taxa de juros: "))
saldo = deposito_inicial
periodo = 24
mes = 1

while mes <= periodo:
    rendimento_mes = saldo * (taxa_juros / 100)
    saldo = saldo + rendimento_mes
    print(f"O valor de lucro no mês {mes} foi de R$ {saldo:5.2f}")
    mes += 1

print(
    f"O total ganho no período de {periodo} mês(es) foi de R$ {saldo:5.2f} com juros a {taxa_juros}%"
)
