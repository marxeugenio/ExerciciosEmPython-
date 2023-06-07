class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
objeto = Retangulo(12,10)

area = objeto.calcular_area()
perimetro = objeto.calcular_perimetro()

print(area)
print(perimetro)