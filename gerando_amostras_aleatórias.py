from numpy.random import default_rng

rng = default_rng()

aleatorio = rng.integers(20, size=(2,4))

print(aleatorio)
