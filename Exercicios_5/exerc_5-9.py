# Escreva um programa que leia dois números.
# Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão.
# Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lemebre-se de que podemos entender o quociente da divisão de dois números como a
# quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

dividendo = int(input("Insira o dividendo: "))
divisor = int(input("Insira o divisor: "))

quociente = 0
resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    quociente = quociente + 1

print(f"Divisão inteira: {quociente}")
print(f"Resto da divisão: {resto}")
