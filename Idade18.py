# Faça um programa que peça a idade do usuário e verifique se ele é maior ou igual a 18 anos.

idade = int(input("Informe a sua idade: "))

if idade > 18:
    print("Você tem mais de 18 anos!")
elif idade == 18:
    print("você tem 18 anos")
else:
    print("MENOR!")