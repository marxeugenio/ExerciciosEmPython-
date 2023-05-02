import numpy as np

# Resolve um sistema de equações lineares
a = np.array([[1,2],[3,4]])
b = np.array([5,6])
x = np.linalg.solve(a,b)

# Calcula os valores singulares de uma matriz
b = np.array([[1,2],[3,4],[5,6]])
U, s, V = np.linalg.svd(b)

# Calcula a decomposição de valores próprios de uma matriz
c = np.array([[1,2],[3,4]])
eigenvalues, engenvectors = np.linalg.eig(c)

print(b)
