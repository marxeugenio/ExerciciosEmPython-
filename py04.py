# Faça um programa que calcule a média aritmética de duas notas e imprima o seu resultado

nota01 = int(input('Informe a sua primeira nota: '))
nota02 = int(input('Informe a sua segunda nota: '))

média = (nota01 + nota02) / 2

print('A média entre a nota um {} e a nota dois {} é {}.'.format(nota01,nota02,média))