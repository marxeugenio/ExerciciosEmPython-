class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")


# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria("João")
conta.depositar(1000)
conta.sacar(500)
conta.consultar_saldo()
