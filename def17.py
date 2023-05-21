lista = ["Marx","Python","Sin","Sum","Night"]

def encontrar_maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
result = (encontrar_maximo(lista))
print(result)

# Resultado é Sum
