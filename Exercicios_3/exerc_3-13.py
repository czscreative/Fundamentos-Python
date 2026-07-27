# Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:
temperatura_celsius = float(input("Informe a temperatura em graus Célsius "))
temperatura_fahrenheit = (9 * (temperatura_celsius / 5)) + 32

print(
    f"A temperatura de {temperatura_celsius}°C convertida em Fahrenheit é {temperatura_fahrenheit}°F"
)
