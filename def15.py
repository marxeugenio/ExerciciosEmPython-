def contar_caracteres(string):
    contador = {}
    for char in string:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador
texto = 'Hello, World!'
resultado = contar_caracteres(texto)
print(resultado)