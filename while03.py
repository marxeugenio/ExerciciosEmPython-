numbers = []
input_number = ''
while input_number != 'done':
    input_number = input("Digite um número (ou 'done' para finalizar): ")
    if input_number != 'done':
        numbers.append(float(input_number))
total = sum(numbers)
average = total / len(numbers)
print(average)
