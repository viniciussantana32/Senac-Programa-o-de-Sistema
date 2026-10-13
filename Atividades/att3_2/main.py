from index import produto1, produto2

print("Escolha um produto:")
print(f"1 - {produto1.nome} - R$ {produto1.preco:.2f}")
print(f"2 - {produto2.nome} - R$ {produto2.preco:.2f}")

opcao = input("Digite o número do produto: ")

if opcao == "1":
	produto_escolhido = produto1
elif opcao == "2":
	produto_escolhido = produto2
else:
	print("Opção inválida.")
	exit()

desconto = 10
preco_final = produto_escolhido.preco_com_desconto(desconto)

print(f"\nProduto escolhido: {produto_escolhido.nome}")
print(f"Valor original: R$ {produto_escolhido.preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor com desconto: R$ {preco_final:.2f}")
