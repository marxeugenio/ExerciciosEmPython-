try:
    resultado = int(input("Digite um número: "))
    resultado = 10 / resultado
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: valor inválido!")
