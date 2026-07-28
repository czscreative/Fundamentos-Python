# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
# O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

import time

contador_foguete = 10

while contador_foguete >= 0:
    print(f'\rContagem: {contador_foguete} ', end='', flush=False)
    time.sleep(1)
    contador_foguete -= 1

print('\rFogo!          ')