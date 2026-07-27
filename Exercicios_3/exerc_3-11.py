# Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
valor_mercadoria = float(input("Informe o valor do produto "))
desconto_mercadoria = float(input("Informe o desconto para o produto "))

valor_desconto = valor_mercadoria * (desconto_mercadoria / 100)
valor_final_mercadoria = valor_mercadoria - valor_desconto

print(
    f"O valor do produto é R$ {valor_mercadoria:5.2f}. O desconto é de {desconto_mercadoria}% que corresponde a R$ {valor_desconto:5.2f}. o valor final do produto é de R$ {valor_final_mercadoria:5.2f}"
)
