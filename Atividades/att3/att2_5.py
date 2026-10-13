class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


pessoa1 = pessoa("Ana", 25)
pessoa2 = pessoa("Carlos", 30)

print(pessoa1.apresentar())
print(pessoa2.apresentar())