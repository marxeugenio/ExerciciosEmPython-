import numpy as np

arr = np.array([1,2,3,4,5])
mask = arr > 2
print(mask)

# Selecionando apenas os elementos maiores que 2
print(arr[mask])