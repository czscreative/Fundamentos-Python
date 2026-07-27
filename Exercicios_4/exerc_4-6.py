# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.
distancia_viagem = int(input("Informar a distância do trajeto a percorrer "))
if distancia_viagem <= 200:
    valor_viagem = distancia_viagem * 0.50
    print(f"O valor total da viagem é de R$ {valor_viagem:5.2f}")
else:
    valor_viagem = distancia_viagem * 0.45
    print(f"O valor total da viagem é de R$ {valor_viagem:5.2f}")
