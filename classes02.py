class Exemplo:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")

objeto = Exemplo("João")
objeto.apresentar()