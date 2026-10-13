class ContaBancaria:
    def __init__(self, titular, saldo=100):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Depósito inválido: o valor deve ser positivo.")  

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saque inválido.")

    def exibir_saldo(self):
        return self.saldo