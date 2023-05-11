import numpy as np

# Cria uma lista com alguns números
numeros = [10, 20, 30, 40, 50]

# Converter a lista em um array do NumPy
array = np.array(numeros)

# Calcular a média e o desvio padrão do array
media = np.mean(array)
desvio_padrao = np.std(array)

# Exibir os resultados
print("Media:", media)
print("Desvio Padrão:", desvio_padrao)