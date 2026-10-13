from attestoque import Estoque

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade em estoque: "))
estoque = Estoque(produto, quantidade)


while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar estoque")
    print("2. Remover estoque")
    print("3. Exibir estoque")
    print("4. Sair")

    opcao = input("Opção: ")
    if opcao == "1":
        quantidade_adicionar = int(input("Digite a quantidade a adicionar: "))
        estoque.adicionar_estoque(quantidade_adicionar)
    elif opcao == "2":
        quantidade_remover = int(input("Digite a quantidade que deseja remover: "))
        estoque.remover_estoque(quantidade_remover)
    elif opcao == "3":
        print(f"Quantidade em estoque de {estoque.produto}: {estoque.exibir_estoque()}")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")