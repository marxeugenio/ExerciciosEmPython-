def dividir (a,b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b
resultado = dividir(10,0)

