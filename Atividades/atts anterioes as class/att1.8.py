esc = int(input("Escolha uma das opções para o menu do seu jogo! \n1 - Iniciando o jogo \n2 - Carregar configurações \n3 - Fechar jogo \nDigite o número da opção desejada: "))
match esc:
    case 1:
        print("Iniciando o jogo...")
    case 2:
        print("Carregando configurações...")
    case 3:
        print("Saindo do jogo...")
    case _:
        print("Opção inválida.")