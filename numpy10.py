import numpy as np

# Cria um array de exemplo
a = np.array([1,2,3,4,5])

# Grava o array em um arquivo de texto
np.savetxt('array.txt',a)

# LÊ o array de um arquivo de texto
b = np.loadtxt('array.txt')

# Grava o array em um arquivo CSV
np.savetxt('array.csv',a,delimiter=',')

# LÊ o array de um arquivo CSV
c = np.loadtxt('array.csv', delimiter=',')

# Grava o array em um arquivo binário
np.save('array.npy',a)

# LÊ o array de um arquivo binário
d = np.load('array.npy')


print(a)
print(b)
print(c)
print(d)