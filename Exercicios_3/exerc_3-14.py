# Exercício 3.14 - Escreva um programa que pergunte a quantiddade de Km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
km_percorrido = int(input("Informe a Quilometragem percorrida "))
dias_aluguel = int(input("Informe por quantos dias o carro foi alugado "))

valor_km_percorrido = km_percorrido * 0.15
valor_dias_aluguel = dias_aluguel * 60

total_pago = valor_km_percorrido + valor_dias_aluguel

print(f"O valor total pago pelo aluguel do carro é de R$ {total_pago:5.2f}.")
