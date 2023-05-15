def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

valores = [5,8,10,3,6]
resultado = calcular_media(valores)
print(resultado)