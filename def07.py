num = int(input("Informe um valor pra ver se ele é primo: "))
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % 1 == 0:
            return False
    return True

if eh_primo(num):
    print("{} é primo".format(num))
else:
    print("{} não é primo".format(num))