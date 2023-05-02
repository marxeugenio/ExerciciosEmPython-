import numpy as np

# Cria uma matriz de exemplo
A = np.array([[1,2],[3,4]])

# Transposição
At = A.T

# Multipicação por escalar
B = 2 * A

# Multiplicação de matrizes
C = np.dot(A,B)

# Inversão
A_inv = np.linalg.det(A)

# Determinante
det_A = np.linalg.det(A)

# Autovalores e autovetores
eigenvalues, eigenvectors = np.linalg.eig(A)
