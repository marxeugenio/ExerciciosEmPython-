import random

target_number = random.randint(1,100)
guess = 0
while guess != target_number:
    guess = int(input("Adibinhe o número: "))
    if guess < target_number:
        print("Muito baixo!")
    elif guess > target_number:
        print("Muito Alto")
print("Parabens! Voce acertou")