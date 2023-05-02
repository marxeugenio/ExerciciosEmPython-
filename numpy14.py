#Indexação e fatiamento
#O NumPy oferece muitas opções para indexar e fatiar arrays. Aqui estão alguns exemplos

import numpy as np

# Cria um array de exemplo 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Acessa um elemento específico
print(a[2,2]) # saida: 6

# Acessa uma linha específica
print(a[1,:]) # saida: [4 5 6]

# Acessa uma coluna específica
print(a[:,1]) # saida [2 5 8]

# Acessa uma submatriz
print(a[:2, 1:]) #saída: [[2 3] [5 6]]
