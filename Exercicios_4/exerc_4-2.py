# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba o valor da multa, cobrando R$ 5 por km acima de da velocidade padrão.
velocidade = int(input("Informe a velocidade do carro na via "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {multa}")
if velocidade < 80:
    print("Dentro do limite de velocidade.")
