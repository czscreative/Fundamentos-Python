# Modifique o programa anterior de forma que o usuário também digite o início e o 
# fim da tabuada, em vez de começar com 1 a 10.

n = int(input('Tabuada de: '))
inicio = int(input('Informe o número inicial: '))
fim = int(input('Informe o número final: '))
while inicio <= fim:
    print(n * inicio)
    inicio = inicio + 1