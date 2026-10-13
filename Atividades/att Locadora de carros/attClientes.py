class Clientes:
    def __init__(self, nome):
        self.nome = nome
        self.historico_locacoes = []

    def registrar_locacao(self, locacao):
        self.historico_locacoes.append(locacao)

    def listar_historico(self):
        if not self.historico_locacoes:
            print(f'{self.nome} ainda não possui locações.')
            return

        for locacao in self.historico_locacoes:
            print(
                f"Veículo: {locacao['modelo']}, "
                f"Placa: {locacao['placa']}, "
                f"Dias: {locacao['dias']}, "
                f"Total: R$ {locacao['valor_total']:.2f}"
            )