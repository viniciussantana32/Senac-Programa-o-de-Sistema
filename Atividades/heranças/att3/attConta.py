class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, saldo=1000, limite=100000):
        super().__init__(saldo)
        self.limite = limite

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f} (Limite: R${self.limite:.2f})")

class ContaPoupanca(Conta):
    def __init__(self, saldo=10, taxa_juros=0.04):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros
    def exibir_saldo(self):
        print(f"Seu saldo é: R$ {self.saldo:.2f}")
    def render_juros(self):
        print(f"Aplicando os R${self.saldo:.2f}, você receberá R${self.saldo * self.taxa_juros:.2f} de juros.")

