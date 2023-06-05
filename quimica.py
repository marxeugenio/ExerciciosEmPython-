class FormulaQuimica:
    def __init__(self, formula):
        self.formula = formula

    def obter_elementos(self):
        elementos = []
        elemento_atual = ""
        for caracter in self.formula:
            if caracter.isupper():
                if elemento_atual != "":
                    elementos.append(elemento_atual)
                elemento_atual = caracter
            elif caracter.islower():
                elemento_atual += caracter
            elif caracter.isdigit():
                elementos.append(elemento_atual + caracter)
                elemento_atual = ""
        if elemento_atual != "":
            elementos.append(elemento_atual)
        return elementos


# Exemplo de uso da classe FormulaQuimica
agua = FormulaQuimica("H2O")
elementos = agua.obter_elementos()
print("Elementos da fórmula:", elementos)
