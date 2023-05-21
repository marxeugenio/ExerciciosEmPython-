numeros = (10,20,30,40,50,60,70,0)

def verificar_sinal(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"
    
resultados = []
for numero in numeros:
    resultado = verificar_sinal(numero)
    resultados.append(resultado)

print(resultados)