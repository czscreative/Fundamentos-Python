# Escreva um programa que leia dosi números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma(+), subtração(-), multiplicação(*) e divisão(/). 
# Exiba o resultado da operação solicitada.

valor_1 = input('Informe o primeiro valor da operação: ')
valor_2 = input('Informe o segundo valor da operação: ')
operacao = input('Informe a operação desejada: ')

if operacao == '+':
    resultado = int(valor_1) + int(valor_2)
elif operacao == '-':
    resultado = int(valor_1) - int(valor_2)
elif operacao == '*':
    resultado = int(valor_1) * int(valor_2)
elif operacao == '/':
    resultado = float(valor_1) / float(valor_2)
else:
    print('Operação não reconhecida pelo sistema! Gentileza informar a operação correta.')

print(f'A operação escolhida foi {operacao} e o resultado foi {resultado}')
