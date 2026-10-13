class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)

produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Smartphone", 1500.00)


