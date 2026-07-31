# Escreva um programa que leia dois números.
# Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

multiplicando = int(input('Insira o multiplicando: '))
multiplicador = int(input('Insira o multiplicador: '))
contador = 0
resultado = 0

while contador < multiplicador:
    resultado  = resultado + multiplicando
    contador = contador + 1

print(f'O resultado é {resultado}')