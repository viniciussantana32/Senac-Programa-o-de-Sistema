class Carro(Veiculo):
    def __init__(self, marca, portas):
        super().__init__(marca)
        self.portas = portas

    def ligar(self):
        print(f"O carro {self.marca} com {self.portas} portas está ligado")