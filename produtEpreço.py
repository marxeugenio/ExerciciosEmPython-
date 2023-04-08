produto01 = input('Insira o primeiro produto: ')
preço01 = int(input('Insira o valor do produto: R$ '))
produto02 = input('Insira o segundo produto: ')
preço02 = int(input('Insira o valor do segundo produto: R$ '))
produto03 = input('Insira o terceiro produto: ')
preço03 = int(input('Insira o terceiro valor: R$ '))

print('O primeiro produto é o {}'.format(produto01))
print('Preço: R${}'.format(preço01))

print('O segundo produto é o {}'.format(produto02))
print('Preço: R${}'.format(preço02))

print('O terceiro produto é o {}'.format(produto03))
print('Preço: R${}'.format(preço03))

if preço01 < preço02 and preço03:
     print('O produto {}, custa {} e é o produto mais barato.'.format(produto01,preço01))

elif preço02 < preço01 and preço03:
    print('O produto {}, custa {} e é o produto mais barato.'.format(produto02,preço02))

else:
    print('O produto {}, custa {} e é o produto mais barato.'.format(produto03,preço03))