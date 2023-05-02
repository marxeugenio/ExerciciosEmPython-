# Faça um programa que peça o nome e a idade do usuário e imprima uma mensagem com essas informações

nome = str(input('Informe o seu nome: '))

idade = int(input('Informe a sua idade para cadastro: '))

print('Seu cadastro foi realizado com sucesso {}, que tem {}.'.format(nome,idade))