num1 = int(input("Informe a primeira nota: "))
num2 = int(input("Informe a segunda nota: "))

print("---------Loading---------")

def calcular_media(num1, num2):
    return(num1 + num2) / 2
média = calcular_media(num1, num2)

print("A sua média foi de {} ".format(média))