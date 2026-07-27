# Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
# Solicita os dados ao usuário
cigarros_por_dia = int(input("Quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Quantidade de anos fumando: "))

# Cálculos intermediários
# 1 ano tem 365 dias
total_dias_fumando = anos_fumando * 365
total_cigarros = cigarros_por_dia * total_dias_fumando

# Cada cigarro reduz 10 minutos de vida
total_minutos_perdidos = total_cigarros * 10

# Conversão de minutos para dias:
# 1 hora = 60 minutos | 1 dia = 24 horas -> 1 dia = 24 * 60 = 1440 minutos
dias_perdidos = total_minutos_perdidos / 1440

# Exibe o resultado formatado com duas casas decimais
print(f"\nTotal de dias de vida perdidos: {dias_perdidos:.2f} dias.")
