class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

c1 = ContaBancaria("João", 1000)
c1.depositar(500)
c2 = ContaBancaria("Maria", 2000)
c2.depositar(1000)
print(f"Saldo de {c1.titular}: R$ {c1.saldo}")
print(f"Saldo de {c2.titular}: R$ {c2.saldo}")