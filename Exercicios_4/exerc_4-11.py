# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar , o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_imovel = float(input("Informe o valor do imóvel desejado: "))
salario_comprador = float(input("Informe o salário do comprador: "))
total_prestacoes = int(input("Informe a quanrtidade de prestações a pagar: "))

valor_maximo_prestacao = (salario_comprador * 30) / 100
valor_prestacao_imovel = valor_imovel / total_prestacoes

if valor_maximo_prestacao >= valor_prestacao_imovel:
    print(
        f"É possível o financiamento. Valor do imóvel: R$ {valor_imovel:5.2f}, Valor das prestações: R$ {valor_prestacao_imovel:5.2f}"
    )
elif valor_maximo_prestacao < valor_prestacao_imovel:
    print(
        f"Não é possível o financiamento. Valor do imóvel: R$ {valor_imovel:5.2f}, Valor das prestações: R$ {valor_prestacao_imovel:5.2f}"
    )
else:
    print("Informações não informadas.")
