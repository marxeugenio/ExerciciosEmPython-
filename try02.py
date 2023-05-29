try:
    resultado = int(input("Digite um valor: "))
    resultado = 10 / resultado
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: valor inválido!")
else:
    print("Resultado:",resultado)