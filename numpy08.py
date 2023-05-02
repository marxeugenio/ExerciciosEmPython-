import numpy as np

# Cria dois arrays de exemplo
a = np.array([True,False,True])
b = np.array([False,True,True])

# Operação AND
c = np.logical_and(a,b)

# Operação OR
d = np.logical_or(a,b)

# Operação NOT
e = np.logical_not(a)

print(a)
print(b)
print(c)
print(d)
print(e)