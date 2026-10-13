class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")
#Classe filha (herança)

class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu sou {self.cargo}.")

f1 = Funcionario("Vinicius", "Desenvolvedor")
f1.apresentar()
f2 = Funcionario("Gabriela", "Analista")
f2.apresentar()