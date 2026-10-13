from attLocadora import Locadora


def main():
    locadora = Locadora()

    locadora.adicionar_veiculo('Fiat Uno', 'ABC-1234', 100.00)
    locadora.adicionar_veiculo('Volkswagen Gol', 'XYZ-5678', 150.00)
    cliente = locadora.adicionar_cliente('Ana')

    print('Veículos cadastrados:')
    locadora.listar_veiculos()

    print()
    print(locadora.locar_veiculo('ABC-1234', cliente))
    print('Veículos após a locação:')
    locadora.listar_veiculos()

    valor_total = locadora.finalizar_locacao('ABC-1234', 3)
    print(f'\nValor da locação por 3 dias: R$ {valor_total:.2f}')

    print('\nHistórico de locações de Ana:')
    cliente.listar_historico()

    print('\nVeículos após a devolução:')
    locadora.listar_veiculos()


if __name__ == '__main__':
    main()