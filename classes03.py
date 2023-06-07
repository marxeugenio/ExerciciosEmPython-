import math


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio **2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
        
objeto = Circulo(10)

area = objeto.calcular_area()
parimetro = objeto.calcular_perimetro()

print(area)
print(parimetro)