# Exercício 4.8 - Reescreva o programa 4.4 e calcule a conta da operadora Tchau usando o ELSE.
plano = input("Qual é o seu plano de celular? ")
if plano == "falapouco":
  minutos_no_plano = 100
  extra = 0.20
  preco = 50
else:
  if plano == "falamuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99

if plano != "falapouco" and plano != "falamuito":
  print("Não conheço este plano")
else:
  if plano == "falapouco" or plano == "falamuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do plano R${preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
      suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento     R${suplemento:10.2f}")
    print(f"Total          R${preco + suplemento:10.2f}")