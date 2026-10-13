from attClientes import Clientes
from attVeiculos import Veiculos


class Locadora:
    def __init__(self):
        self.veiculos = []
        self.clientes = []
        self.locacoes_ativas = {}

    def adicionar_veiculo(self, modelo, placa, valor_diaria):
        if valor_diaria <= 0:
            raise ValueError('O valor da diária deve ser maior que zero.')
        if any(veiculo.placa == placa for veiculo in self.veiculos):
            raise ValueError(f'Já existe um veículo cadastrado com a placa {placa}.')

        veiculo = Veiculos(modelo, placa, valor_diaria)
        self.veiculos.append(veiculo)
        return veiculo

    def adicionar_cliente(self, nome):
        cliente = Clientes(nome)
        self.clientes.append(cliente)
        return cliente

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            situacao = 'Disponível' if veiculo.disponivel else 'Alugado'
            print(
                f'Modelo: {veiculo.modelo}, Placa: {veiculo.placa}, '
                f'Diária: R$ {veiculo.valor_diaria:.2f}, Situação: {situacao}'
            )

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f'Nome: {cliente.nome}')

    def locar_veiculo(self, placa, cliente):
        veiculo = next(
            (veiculo for veiculo in self.veiculos if veiculo.placa == placa),
            None
        )
        if veiculo is None:
            raise ValueError(f'Não existe veículo cadastrado com a placa {placa}.')
        if not veiculo.disponivel:
            raise ValueError(f'O veículo com a placa {placa} já está alugado.')
        if cliente not in self.clientes:
            raise ValueError('O cliente precisa estar cadastrado na locadora.')

        veiculo.disponivel = False
        self.locacoes_ativas[placa] = {
            'veiculo': veiculo,
            'cliente': cliente
        }
        return f'{veiculo.modelo} alugado para {cliente.nome}.'

    def finalizar_locacao(self, placa, quantidade_dias):
        if not isinstance(quantidade_dias, int) or quantidade_dias <= 0:
            raise ValueError('A quantidade de dias deve ser um inteiro maior que zero.')

        locacao = self.locacoes_ativas.get(placa)
        if locacao is None:
            raise ValueError(f'Não há locação ativa para o veículo com a placa {placa}.')

        veiculo = locacao['veiculo']
        cliente = locacao['cliente']
        valor_total = veiculo.valor_diaria * quantidade_dias
        cliente.registrar_locacao({
            'modelo': veiculo.modelo,
            'placa': veiculo.placa,
            'dias': quantidade_dias,
            'valor_total': valor_total
        })

        veiculo.disponivel = True
        del self.locacoes_ativas[placa]
        return valor_total