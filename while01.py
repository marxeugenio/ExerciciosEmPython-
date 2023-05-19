age = -1
while age < 0 or age > 120:
    age = int(input("Digite sua idade: "))
    if age < 0 or age > 120:
        print("Idade invalida. Tente novamente")
print("Idade valida")