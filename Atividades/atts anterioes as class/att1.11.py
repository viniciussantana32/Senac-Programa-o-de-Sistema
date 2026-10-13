secreto = 7

for i in range(1,4):
    chute = int(input("Digite um número entre 1 e 10: "))
    if chute == secreto:
        print("Parabéns! Você acertou!")
        break
    elif chute < secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")
    if chute != secreto and i == 3:
        print("Suas tentativas acabaram. O número secreto era:", secreto)