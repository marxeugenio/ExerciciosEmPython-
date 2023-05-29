try:
    resultado = int(input("digite um número: "))
    resultado = 10 / resultado
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: valor inválido!")
else:
    print("Resultado é:",resultado)
finally:
    print("Finalizando o programa.")