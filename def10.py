def encontrar_menor_valor(lista):
    menor_valor = lista[0]
    for valor in lista:
        if valor < menor_valor:
            menor_valor = valor
        return menor_valor

lista_numeros = [4,7,2,9,1]
resultado = encontrar_menor_valor(lista_numeros)
print(resultado)