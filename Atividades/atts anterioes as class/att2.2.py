def eh_primo(numero):
	if numero < 2:
		return False

	for divisor in range(2, numero):
		if numero % divisor == 0:
			return False

	return True


def menor_primo_maior_que(numero):
	candidato = numero + 1

	while not eh_primo(candidato):
		candidato += 1

	return candidato


numero = int(input("Digite um número inteiro: "))
print(f"O menor número primo maior que {numero} é {menor_primo_maior_que(numero)}")
