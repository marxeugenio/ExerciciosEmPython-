# Faça um programa que peça a temperatura em graus Celsius e a converta para Fahrenheit. A fórmula de conversão é: F = (C *1.8) + 32

temperatura = int(input('Informe a temperatura em Graus Celsius: '))
Fahrenheit = int(temperatura * 1.8) + 32

print('Convertendo a Graus Celsius que é {}, para Fahrenheit fica {}.'.format(temperatura,Fahrenheit))
