def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

resultado = calcular_fatorial(5)
print(resultado)