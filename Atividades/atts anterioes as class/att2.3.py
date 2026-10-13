class ClassesRpg:
    def __init__(self, classe, poder, dano):
        self.classe = classe
        self.poder = poder
        self.dano = dano

    def apresentar(self):
        return f"Olá, sou um {self.classe} e tenho o poder de {self.poder} e tenho {self.dano} de dano."

p1 = ClassesRpg("Mago", "magia", 100)
p2 = ClassesRpg("Barbaro", "furia", 150)
p3 = ClassesRpg("Paladino", "justiça", 120)

print(p1.apresentar())
print(p2.apresentar())
print(p3.apresentar())
