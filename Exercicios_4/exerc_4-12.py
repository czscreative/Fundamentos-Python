# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade em kWh consumida e o tipo de instalação. R = Residência, I = Indústria e C = Comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.
# =================================================
# == Tipo        === Faixa (kWh)    === Preço   ===
# == Residencial === Até 500        === R$ 0,40 ===
#                === Acima de 500   === R$ 0,65 ===
# == Comercial   === Até 1000       === R$ 0,55 ===
#                === Acima de 1000  === R$ 0,60 ===
# == Industrial  === Até 5000       === R$ 0,55 ===
#                === Acima de 5000  === R$ 0,60 ===
# =================================================

total_kwh_consumido = int(input("Informe o total de kWh consumidos: "))
tipo_instalacao = input(
    "Informe o tipo de instalação. R - Residencial, C - Comercial e I - Industrial: "
)

if tipo_instalacao == "R":
    if total_kwh_consumido <= 500:
        total_a_pagar = total_kwh_consumido * 0.40
    else:
        total_a_pagar = total_kwh_consumido * 0.65
    tipo_instalacao = "Residencial"
elif tipo_instalacao == "C":
    if total_kwh_consumido <= 1000:
        total_a_pagar = total_kwh_consumido * 0.55
    else:
        total_a_pagar = total_kwh_consumido * 0.60
    tipo_instalacao = "Comercial"
elif tipo_instalacao == "I":
    if total_kwh_consumido <= 5000:
        total_a_pagar = total_kwh_consumido * 0.55
    else:
        total_a_pagar = total_kwh_consumido * 0.60
    tipo_instalacao = "Industrial"
else:
    print("Tipo de instalação não informado! Gentileza informar o tipo.")

print(
    f"Para o tipo {tipo_instalacao} o valor total é de R$ {total_a_pagar:5.2f} por {total_kwh_consumido} kWh."
)
