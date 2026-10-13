class Contabancaria:
    def __init__(self, saldo_inicial):
        self.__saldo_publico = saldo_inicial
        self.__saldo_Nprivado = saldo_inicial
        self.__saldo_privado = saldo_inicial


    def depositar(self, valor):
        if valor > 0:
            self.__saldo_publico += valor

    def get_saldo(self):
        return self.__saldo_publico

conta = Contabancaria(1000)
conta.depositar(500)
print(conta.get_saldo())