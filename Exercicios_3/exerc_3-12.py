'''Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.'''

distancia = int(input("Informe a distância da viagem "))
velocidade_media = int(input("Informe a velocidade média esperada "))

tempo_viagem = distancia / velocidade_media

print(f"O tempo de viagem para uma distância de {distancia}Km e a velocidade média de {velocidade_media}Km/h é de {tempo_viagem}h")