class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        informacoes = (
            f"Marca: {self.marca} | "
            f"Modelo: {self.modelo} | "
            f"Ano: {self.ano}"
        )
        print(informacoes)

carro1 = carro("Toyota", "Corolla", 2020)
carro2 = carro("Honda", "Civic", 2019)

print("Informações do carro 1:")
carro1.exibir_informacoes()
print("Informações do carro 2:")
carro2.exibir_informacoes()
