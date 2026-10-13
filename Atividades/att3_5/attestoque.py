class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
        else:
            print("Quantidade inválida: o valor deve ser positivo.")

    def remover_estoque(self, quantidade):
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print("Quantidade inválida: o valor deve ser positivo e menor ou igual à quantidade em estoque.")

    def exibir_estoque(self):
        return self.quantidade